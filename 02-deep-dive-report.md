## 3.2. Problem Statement (6-field) & Metrics

> ⏱ 15 phút

| Field | Nội dung chi tiết |
|-------|-------------------|
| **Actor / Operator** | Nhân viên CSKH Xanh SM xử lý ticket hằng ngày.<br>Người chịu ảnh hưởng gián tiếp: tài xế (chờ giải quyết thu nhập) và khách hàng (chờ phản hồi). |
| **Current Workflow** | Nhận ticket, tự phân loại, tra cứu thủ công trên nhiều công cụ nội bộ (chuyến đi, GPS, giao dịch, thu nhập), áp chính sách, soạn phản hồi theo mẫu rồi đóng ticket.<br>Tổng **~7,5 phút/ticket**. |
| **Bottleneck** | **Bước 3**, tra cứu chéo nhiều hệ thống (~4,5 phút/ticket, dễ sót hoặc sai dữ liệu). |
| **Business Impact** | Giả định 100.000 ticket/tháng, 60–70% thuộc nhóm lặp, ~7,5 phút/ticket, tương đương khoảng **7.500–8750 giờ công/tháng**. |
| **Success Metric** | 1. CSAT (Customer Satisfaction Score) không thấp hơn baseline.<br>2. 85% ticket nhóm lặp được phân loại đúng trong dưới 10 giây.<br>3. Thời gian xử lý trung bình nhóm lặp giảm từ ~8 phút xuống dưới 2 phút. |
| **Operational Boundary** | ✅ **Được phép:** phân loại, trích xuất thông tin, truy xuất dữ liệu (chỉ đọc), soạn phản hồi, tự giải quyết ca đơn giản trong ngưỡng chính sách.<br>⛔ **Tuyệt đối không:** tự hoàn tiền hoặc điều chỉnh thu nhập vượt ngưỡng; kết luận kỷ luật hay khóa tài khoản tài xế; tiết lộ dữ liệu cá nhân của bên còn lại; tự sửa dữ liệu gốc.<br>👤 **Cần người duyệt:** ca tranh chấp, ca liên quan an toàn hoặc khiếu nại nghiêm trọng, ca vượt ngưỡng số tiền, ca AI không tự tin. |

---

## 3.3. Future-State Flow & AI Fit

> ⏱ 25 phút

### AI-Fit Matrix

☐ Rule / State-Machine  ·  ☐ LLM Feature  ·  ☑ **Agentic Loop**

**Lý do chọn:** bài toán cần gọi nhiều hệ thống (chuyến đi, GPS, giao dịch) rồi quyết định theo ngữ cảnh. Phần quyết định chính sách nên chạy bằng rule cứng bên trong agent để kiểm soát được.

> 💡 **Phương án nhẹ hơn cho POC:** bắt đầu ở mức LLM Feature + Rule (phân loại và soạn nháp), chưa cho agent tự truy xuất.

### Future-State Flow

Chú thích: 🔵 AI · 🟢 Con người

```text
 [1] Nhận ticket
        │
        v
 [2] 🔵 AI: phân loại + trích xuất (mã chuyến, loại khiếu nại)
        │──── confidence thấp ───> ↩️ 🟢 CSKH phân loại tay
        v
 [3] 🔵 AI Agent: truy xuất chuyến đi/GPS/giao dịch/thu nhập (chỉ đọc)
        │──── tool lỗi hoặc thiếu dữ liệu ───> ↩️ retry 1 lần ──> 🟢 CSKH
        v
 [4] 🔵 AI + rule chính sách: đề xuất quyết định
        │
        ├── ca đơn giản, trong ngưỡng ──> [5a] 🔵 AI tự soạn và gửi, ghi log
        │
        └── tranh chấp / vượt ngưỡng / nhạy cảm / không tự tin
                 ──> [5b] 🟢 CSKH duyệt bản nháp AI rồi gửi
        │
        v
 [6] 🟢 QA lấy mẫu 5-10% ticket tự động để kiểm tra chất lượng
```

---

# 🏁 Phase 5 — EVALUATE

> **Nhóm · 20 phút**

## AI Readiness Checklist

- [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
- [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
- [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

- ☐ **GO** (Bắt đầu xây dựng Prototype): bắt đầu phát triển với scope hẹp.
- ☑ **NOT YET** (Cần tích lũy thêm dữ liệu/xác lập baseline): trì hoãn để chuẩn bị thêm.
- ☐ **NO-GO** (Không khả thi / Rule-based tốt hơn): hủy bỏ dự án AI này.

## Justification

*Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí.*

**Giá trị bài toán.** Bài toán có giá trị rõ. Khối lượng ticket lớn, nhóm ticket lặp chiếm phần đa số (giả định 60–70%), và bước nghẽn chính (tra cứu chéo nhiều hệ thống, ~5 phút/ticket) là việc agent làm tốt hơn người. Các ca có quy tắc cứng nên xử lý bằng rule, LLM chỉ dùng cho phân loại và soạn phản hồi, vừa rẻ vừa dễ kiểm soát.

**Vì sao chưa phải GO.** Chưa xác nhận có dữ liệu ticket và log sạch để làm bộ test, nên chưa đo được các ngưỡng trong Success Metric. Chưa có baseline thật (~8 phút/ticket mới là ước tính) và chưa có đồng thuận của CSKH và tài chính/vận hành về ngưỡng cho AI tự giải quyết. Chi phí suy luận và tích hợp hệ thống cũng chưa được ước lượng.

**Rủi ro trong tầm kiểm soát.** AI chỉ có quyền đọc, có HITL cho ca nhạy cảm, fallback về xử lý thủ công, QA lấy mẫu và kill-switch.

**Điều kiện chuyển sang GO (2–4 tuần).**

1. Lấy mẫu và gán nhãn ticket lịch sử.
2. Đo baseline thật.
3. Chốt ngưỡng tự giải quyết với stakeholder.
4. Ước lượng chi phí.

Sau đó xây prototype scope hẹp (2–3 loại ticket lặp, chạy shadow mode trước khi bật tự gửi).