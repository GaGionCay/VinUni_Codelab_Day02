# Lenses tìm bài toán AI cho Vingroup và QUICK-ASSESS
## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)
**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**.
Tôi là **Ánh**, **AI Product Engineer** tại **Vin Smart Future** đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng Vinhomes.
# 🔍 Phase 1 — SCAN (Cá nhân)

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | Tốn thời gian | Tự động tổng hợp, chẩn đoán sự cố và gợi ý phương án sửa chữa cho Kỹ thuật viên |
| 2 | Vinhomes | AI có thể tốt hơn | Tự động phân tích camera thời gian thực để phát hiện sự cố an ninh và rủi ro an toàn không gian công cộng |
| 3 | Xanh SM | Tốn thời gian | Lập lịch bảo dưỡng định kỳ và quản trị sức khỏe pin xe điện |
| 4 | Vinmec | AI có thể tốt hơn | Tự động theo dõi & Chăm sóc bệnh nhân từ xa sau xuất viện |
| 5 | VinFast | Lặp lại | Tự động phân tích phản hồi khách hàng đa kênh để định hướng R&D phần mềm |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Tự động tổng hợp, chẩn đoán sự cố và gợi ý phương án sửa      │
│ chữa cho Kỹ thuật viên (Smart Maintenance Copilot)                      │
│ Công ty thành viên: [x] Vinhomes (Khối Vận hành & Kỹ thuật Tòa nhà)     │
│                                                                         │
│ Ai đang đau? Kỹ thuật viên (mất thời gian tra cứu O&M/BIM), Cư dân      │
│ (chờ đợi thang máy/máy bơm sửa xong)                                    │
│                                                                         │
│ Workflow thủ công hiện hiện tại (5 bước):                               │
│   1. Tiếp nhận cảnh báo sự cố từ BMS hoặc phản ánh từ BQL               │
│   → 2. Kỹ thuật viên di chuyển tới hiện trường kiểm tra hiện trạng      │
│   → 3. Tra cứu thủ công tài liệu O&M, bản vẽ CAD/BIM, lịch sử bảo trì   │
│   → 4. Chẩn đoán nguyên nhân rễ cây (Root-cause) và lập phương án sửa   │
│   → 5. Báo cáo đề xuất vật tư thay thế và chờ duyệt thi công            │
│                                                                         │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 30 - 45 phút/sự cố)                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4                          │
│ (RAG tra cứu tức thì sơ đồ/O&M -> GenAI phân tích dấu hiệu & gợi ý      │
│  quy trình sửa chữa + list vật tư)                                      │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Giảm MTTR (Mean Time to Repair) từ 60 phút ──> dưới 25 phút.          │
│ • Tăng tỷ lệ sửa đúng ngay lần đầu (First-Time Fix Rate) ──> > 85%.     │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (RAG Copilot tra cứu & chẩn đoán)   │
└─────────────────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Tự động phân tích camera thời gian thực để phát hiện sự cố    │
│ an ninh và rủi ro an toàn không gian công cộng                          │
│ Công ty thành viên: [x] Vinhomes (Khối An ninh & An toàn KĐT)           │
│                                                                         │
│ Ai đang đau? Nhân viên an ninh trung tâm (mỏi mắt, bỏ sót rủi ro),      │
│ Đội tuần tra (bị động), Cư dân (gặp nguy hiểm ngã bể bơi/trộm cắp)      │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Bảo vệ trực ca ngồi dòm hàng chục màn hình camera 24/7             │
│   → 2. Phát hiện bằng mắt thường các bất thường (nếu không xao nhãng)   │
│   → 3. Xóa xác nhận vị trí camera xảy ra sự cố trên sơ đồ KĐT           │
│   → 4. Đàm thoại bộ đàm báo cho đội tuần tra cơ động gần nhất           │
│   → 5. Đội tuần tra tiếp cận hiện trường để xử lý sự cố                 │
│                                                                         │
│ Bước nào tốn nhất? Bước 1-2 (⏱ 10 - 20 phút trễ phản ứng hoặc bỏ sót)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-2-3                        │
│ (Computer Vision quét camera 24/7 -> Tự động phát hiện bất thường       │
│  -> Tự động định vị và phát cảnh báo tới app Đội tuần tra)              │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Giảm thời gian phát hiện & phản ứng sự cố từ 15 phút ──> dưới 1 phút. │
│ • Tỷ lệ phát hiện sự cố nguy hiểm (ngã bể bơi, đột nhập) ──> > 95%.     │
│                                                                         │
│ Quick Architecture: [x] Predictive Model / Vision AI (Video Analytics)  │
└─────────────────────────────────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Lập lịch bảo dưỡng định kỳ và quản trị sức khỏe pin xe điện   │
│                                                                         │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau? Đội quản lý đội xe (thiếu dữ liệu pin), Kỹ thuật viên      │
│ xưởng (quá tải đột xuất), Tài xế (nguy cơ nằm đường)                    │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Theo dõi số km vận hành xe qua báo cáo định kỳ thủ công            │
│   → 2. Đợi xe đạt mốc km cố định (10k, 20k km) hoặc chờ xe báo lỗi      │
│   → 3. Điều phối viên gọi tài xế đem xe về xưởng dịch vụ Xanh SM        │
│   → 4. Kỹ thuật viên cắm máy đọc lỗi và đánh giá thủ công SOH pin       │
│   → 5. Xếp lịch thay thế/bảo dưỡng phụ tùng hoặc cell pin hỏng          │
│                                                                         │
│ Bước nào tốn nhất? Bước 2-4 (⏱ Tốn 2 - 3 ngày dừng xe / hỏng hóc nặng) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-2-3                        │
│ (ML phân tích Telemetry thời gian thực -> Dự báo suy hao SOH pin        │
│  -> Tự động điều phối lịch bảo dưỡng né giờ cao điểm kinh doanh)        │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Giảm chi phí sửa chữa khẩn cấp & hỏng pin nặng ──> 20%.               │
│ • Giảm thời gian xe nằm xưởng (Downtime) từ 48 giờ ──> dưới 12 giờ.     │
│                                                                         │
│ Quick Architecture: [x] Predictive Model (Time-series Anomaly ML)       │
└─────────────────────────────────────────────────────────────────────────┘
```
---