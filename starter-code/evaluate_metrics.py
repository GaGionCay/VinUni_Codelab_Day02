"""Evaluate annotated offline frame logs. Standard library only."""

import math


THRESHOLDS = {
    "sign_iou": 0.5,
    "sign_deadline_ms": 1000,
    "sign_precision": 0.95,
    "sign_timely_recall": 0.95,
    "lane_max_error": 0.02,
    "lane_pair_accuracy": 0.90,
    "latency_p95_ms": 100,
}


def require_number(value, name, minimum=0, maximum=math.inf):
    if type(value) not in (int, float) or not math.isfinite(value) or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be finite and between {minimum} and {maximum}.")


def validate_sign(sign, reference):
    fields = {"label", "bbox"}
    if reference:
        fields |= {"instance_id", "first_readable_ms"}
    if not isinstance(sign, dict) or set(sign) != fields:
        raise ValueError("Invalid traffic sign fields.")
    if not isinstance(sign["label"], str) or not sign["label"].strip():
        raise ValueError("A sign requires a label.")
    box = sign["bbox"]
    if not isinstance(box, list) or len(box) != 4:
        raise ValueError("bbox must have four normalized coordinates.")
    for value in box:
        require_number(value, "bbox", maximum=1)
    if box[0] >= box[2] or box[1] >= box[3]:
        raise ValueError("bbox must have positive width and height.")
    if reference:
        if not isinstance(sign["instance_id"], str) or not sign["instance_id"].strip():
            raise ValueError("Reference sign requires instance_id.")
        require_number(sign["first_readable_ms"], "first_readable_ms")


def validate_lanes(lanes):
    if not isinstance(lanes, dict) or set(lanes) != {"left", "right"}:
        raise ValueError("Lane data requires left and right.")
    for coordinates in lanes.values():
        if coordinates is None:
            continue
        if not isinstance(coordinates, list) or len(coordinates) != 3:
            raise ValueError("Use x coordinates at y/H = 0.6, 0.75, 0.9, or null.")
        for value in coordinates:
            require_number(value, "lane x/W", maximum=1)
    if lanes["left"] is not None and lanes["right"] is not None:
        if any(left >= right for left, right in zip(lanes["left"], lanes["right"])):
            raise ValueError("Left boundary must be left of right boundary.")


def validate_log(log):
    fields = {"clip_id", "data_source", "sign_classes", "frames"}
    if not isinstance(log, dict) or set(log) != fields:
        raise ValueError("Log requires clip_id, data_source, sign_classes, frames.")
    if not isinstance(log["clip_id"], str) or not log["clip_id"].strip():
        raise ValueError("clip_id must be a nonempty string.")
    if log["data_source"] not in {"synthetic", "measured"}:
        raise ValueError("data_source must be synthetic or measured.")
    classes = log["sign_classes"]
    if (
        not isinstance(classes, list) or not classes
        or not all(isinstance(value, str) and value.strip() for value in classes)
        or len(set(classes)) != len(classes)
    ):
        raise ValueError("Provide unique sign classes.")
    if not isinstance(log["frames"], list):
        raise ValueError("frames must be a list.")
    seen_frames = set()
    seen_instances = {}
    for frame in log["frames"]:
        required = {
            "frame_id", "capture_ms", "available_ms", "reference_signs",
            "predicted_signs", "reference_lanes", "predicted_lanes",
        }
        if not isinstance(frame, dict) or set(frame) != required:
            raise ValueError("Invalid frame fields.")
        if not isinstance(frame["frame_id"], str) or not frame["frame_id"].strip():
            raise ValueError("frame_id must be a nonempty string.")
        if frame["frame_id"] in seen_frames:
            raise ValueError("Duplicate frame_id.")
        seen_frames.add(frame["frame_id"])
        require_number(frame["capture_ms"], "capture_ms")
        require_number(frame["available_ms"], "available_ms", minimum=frame["capture_ms"])
        for field, reference in (("reference_signs", True), ("predicted_signs", False)):
            if not isinstance(frame[field], list):
                raise ValueError("Sign records must be lists.")
            instance_ids = set()
            for sign in frame[field]:
                validate_sign(sign, reference)
                if sign["label"] not in classes:
                    raise ValueError("Sign label is outside declared scope.")
                if reference:
                    instance_id = sign["instance_id"]
                    if instance_id in instance_ids:
                        raise ValueError("Duplicate reference instance in frame.")
                    instance_ids.add(instance_id)
                    identity = (sign["label"], sign["first_readable_ms"])
                    if seen_instances.get(instance_id, identity) != identity:
                        raise ValueError("Reference identity changes across frames.")
                    seen_instances[instance_id] = identity
                    if sign["first_readable_ms"] > frame["capture_ms"]:
                        raise ValueError("Reference sign precedes readable onset.")
        validate_lanes(frame["reference_lanes"])
        validate_lanes(frame["predicted_lanes"])


def box_iou(first, second):
    width = max(0, min(first[2], second[2]) - max(first[0], second[0]))
    height = max(0, min(first[3], second[3]) - max(first[1], second[1]))
    intersection = width * height
    first_area = (first[2] - first[0]) * (first[3] - first[1])
    second_area = (second[2] - second[0]) * (second[3] - second[1])
    return intersection / (first_area + second_area - intersection)


def match_signs(references, predictions):
    candidates = []
    for reference_index, reference in enumerate(references):
        for prediction_index, prediction in enumerate(predictions):
            overlap = box_iou(reference["bbox"], prediction["bbox"])
            if reference["label"] == prediction["label"] and overlap >= THRESHOLDS["sign_iou"]:
                candidates.append((overlap, reference_index, prediction_index))
    matched_references = set()
    matched_predictions = set()
    for _, reference_index, prediction_index in sorted(candidates, reverse=True):
        if reference_index not in matched_references and prediction_index not in matched_predictions:
            matched_references.add(reference_index)
            matched_predictions.add(prediction_index)
    return matched_references


def evaluate_metrics(log):
    validate_log(log)
    true_positives = false_positives = false_negatives = 0
    lane_eligible = lane_correct = 0
    encountered = {label: set() for label in log["sign_classes"]}
    timely = {label: set() for label in log["sign_classes"]}
    latencies = []
    for frame in log["frames"]:
        references = frame["reference_signs"]
        predictions = frame["predicted_signs"]
        matched = match_signs(references, predictions)
        true_positives += len(matched)
        false_positives += len(predictions) - len(matched)
        false_negatives += len(references) - len(matched)
        for index, sign in enumerate(references):
            encountered[sign["label"]].add(sign["instance_id"])
            deadline = sign["first_readable_ms"] + THRESHOLDS["sign_deadline_ms"]
            if index in matched and frame["available_ms"] <= deadline:
                timely[sign["label"]].add(sign["instance_id"])
        reference_lanes = frame["reference_lanes"]
        predicted_lanes = frame["predicted_lanes"]
        if all(value is not None for value in reference_lanes.values()):
            lane_eligible += 1
            correct = all(
                predicted_lanes[side] is not None
                and all(
                    abs(reference - prediction) <= THRESHOLDS["lane_max_error"]
                    for reference, prediction in zip(reference_lanes[side], predicted_lanes[side])
                )
                for side in ("left", "right")
            )
            lane_correct += int(correct)
        latencies.append(frame["available_ms"] - frame["capture_ms"])
    precision = None
    if true_positives + false_positives:
        precision = true_positives / (true_positives + false_positives)
    recalls = [
        {
            "label": label,
            "encounters": len(encountered[label]),
            "timely_hits": len(timely[label]),
            "recall": len(timely[label]) / len(encountered[label]) if encountered[label] else None,
        }
        for label in log["sign_classes"]
    ]
    return {
        "clip_id": log["clip_id"],
        "data_source": log["data_source"],
        "frame_count": len(log["frames"]),
        "sign_tp": true_positives,
        "sign_fp": false_positives,
        "sign_fn": false_negatives,
        "sign_precision": precision,
        "sign_timely_recall_by_class": recalls,
        "lane_eligible_frames": lane_eligible,
        "lane_correct_frames": lane_correct,
        "lane_pair_accuracy": lane_correct / lane_eligible if lane_eligible else None,
        "latency_p95_ms": sorted(latencies)[math.ceil(0.95 * len(latencies)) - 1] if latencies else None,
    }


def derive_issues(metrics):
    issues = []
    if metrics["sign_precision"] is None:
        issues.append("SIGN_PRECISION_UNAVAILABLE")
    elif metrics["sign_precision"] < THRESHOLDS["sign_precision"]:
        issues.append("SIGN_PRECISION_BELOW_TARGET")
    if any(row["recall"] is None for row in metrics["sign_timely_recall_by_class"]):
        issues.append("SIGN_RECALL_UNAVAILABLE")
    if any(
        row["recall"] is not None and row["recall"] < THRESHOLDS["sign_timely_recall"]
        for row in metrics["sign_timely_recall_by_class"]
    ):
        issues.append("SIGN_RECALL_BELOW_TARGET")
    if metrics["lane_pair_accuracy"] is None:
        issues.append("LANE_METRIC_UNAVAILABLE")
    elif metrics["lane_pair_accuracy"] < THRESHOLDS["lane_pair_accuracy"]:
        issues.append("LANE_PAIR_BELOW_TARGET")
    if metrics["latency_p95_ms"] is None:
        issues.append("LATENCY_UNAVAILABLE")
    elif metrics["latency_p95_ms"] > THRESHOLDS["latency_p95_ms"]:
        issues.append("LATENCY_P95_ABOVE_TARGET")
    return issues
