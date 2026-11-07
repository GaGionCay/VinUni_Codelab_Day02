# Lab 02 · Problem Scan và Quick Problem Cards

Bối cảnh bài lab là Vin Smart Future. Các pain point là giả thuyết để khảo sát, các ngưỡng là mục tiêu đề xuất. Nhóm chưa xác minh quy trình nội bộ hoặc hiệu năng thực tế của VinFast.

## Phase 1 · SCAN

| # | Đơn vị | Lens | Bài toán và tác động cần kiểm chứng |
|---|---|---|---|
| 1 | VinFast | AI có thể tốt hơn | Mô hình từ camera trước nhận sai hoặc bỏ sót biển báo, nhận sai hai vạch biên làn và trả kết quả trễ. Mô-đun lập kế hoạch hoặc người lái nhận thông tin thiếu, sai hoặc muộn. |
| 2 | VinFast | Lặp lại | Nhân viên đối soát ghép các phiên sạc với hóa đơn để tìm dòng lệch. |
| 3 | VinFast | Tốn thời gian | Nhân viên hỗ trợ đọc mô tả triệu chứng và xác định bộ phận kỹ thuật tiếp nhận. |
| 4 | Xanh SM | Pain từ người khác | Tài xế phải xác nhận lại điểm đón khi ghi chú và vị trí trên bản đồ không khớp. |
| 5 | Vinhomes | Lặp lại | Nhân viên phân loại phản ánh cư dân để chuyển bộ phận phụ trách. |

## Phase 2 · Card 1 · Nhận diện biển báo và vạch làn đúng, kịp thời

- **Actor** — Nhóm kỹ sư phát triển và kiểm thử hệ thống xe tự lái.
- **Thành phần nhận kết quả** — Mô-đun lập kế hoạch và giao diện thông báo mô phỏng cho người lái.
- **Current workflow** — Nhận khung hình → tiền xử lý → suy luận biển báo và vạch làn → hậu xử lý → chuyển kết quả đến thành phần nhận.
- **Bottleneck** — Dự đoán sai hoặc bỏ sót tại nhánh nhận diện. Hàng đợi, suy luận hoặc bước truyền và hiển thị có thể gây trễ. Cần đo thời gian từng bước để xác định nguyên nhân.
- **Điểm can thiệp** — Cải thiện mô hình Computer Vision và pipeline dựa trên lỗi đo được. Prototype Gemini của lab đọc metric do Python tính để tạo báo cáo nháp có ranh giới.
- **Metric đề xuất** — Precision biển ≥95%, recall đúng hạn ≥95% mỗi loại, tỷ lệ đúng cả hai vạch ≥90%, độ trễ p95 ≤100 ms trên thiết bị mục tiêu. Xem quy tắc đo trong Deep-Dive.
- **Quick architecture** — Computer Vision kết hợp xử lý và kiểm tra bằng Rule. LLM Feature hỗ trợ báo cáo kiểm thử offline.

## Card 2 · Đối chiếu hóa đơn sạc

- **Actor** — Nhân viên đối soát.
- **Workflow** — Nhận bảng → chuẩn hóa mã phiên → ghép bản ghi → kiểm tra lệch → chuyển ca chưa khớp.
- **Bottleneck** — Ghép phiên và kiểm tra dòng lệch. Chưa có số đo phút/lô.
- **Điểm can thiệp và kiến trúc** — Rule ghép theo mã phiên, đối chiếu theo ngưỡng đã chốt.
- **Metric đề xuất** — Giảm ≥25% phút/lô và phát hiện ≥95% dòng lệch trên mẫu có nhãn.

## Card 3 · Phân loại mô tả lỗi xe

- **Actor** — Nhân viên hỗ trợ kỹ thuật.
- **Workflow** — Nhận phản ánh → đọc triệu chứng → gán nhóm → xác nhận → chuyển kỹ thuật viên.
- **Bottleneck** — Mô tả tự do cần đọc và phân loại. Chưa có số đo giây/phiếu.
- **Điểm can thiệp và kiến trúc** — LLM Feature gợi ý nhóm từ nội dung phiếu. Nhân viên xác nhận.
- **Metric đề xuất** — ≥90% gợi ý trùng nhóm tham chiếu và giảm ≥25% giây/phiếu.

## Đề xuất cá nhân trước buổi họp

Chọn Card 1 vì đề tài tập trung vào chất lượng và độ trễ của mô hình nhận thức môi trường. Kinh nghiệm YOLOv8 trước đây có thể hỗ trợ nhánh biển báo. Vẫn cần dữ liệu vạch làn có nhãn, log thời gian và thiết bị mục tiêu.

Card 2 có thể bắt đầu với Rule. Card 3 cần bộ phiếu và nhãn kỹ thuật. Cả ba cần dữ liệu thật để xác minh tính khả thi. Đề xuất này dùng để nhóm so sánh trước khi chọn idea chung.
