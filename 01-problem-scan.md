# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)
### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
| 1 | Vinmec | Tốn thời gian | Bác sĩ và điều dưỡng nhập tay bệnh sử, kê đơn, tóm tắt xuất viện,... gây tốn rất nhiều thời gian |
| 2 | VinFast | Pain từ người khác | Chẩn đoán lỗi và tra cứu tài liệu kỹ thuật tại xưởng làm bằng tay, tỷ lệ sửa đúng ngay lần đầu thấp nên nhiều xe phải quay lại xưởng |
| 3 | Xanh SM | Lặp lại | Nhân viên CSKH xử lý tay lượng lớn ticket lặp (thất lạc đồ, sai cước, tranh chấp thu nhập tài xế), tốn nhiều giờ công cho các ca có quy tắc rõ ràng |
| 4 | Vinhomes | Tốn thời gian | Kiểm tra tay hồ sơ pháp lý, hợp đồng và lịch thanh toán khi mở bán, dễ sai sót và phải làm lại, nghẽn nhất vào tháng cao điểm |
| 5 | Vinhomes | Pain từ người khác | Bảo trì thang máy, HVAC theo lịch cố định hoặc chờ sự cố mới xử lý, thiếu dự báo hỏng hóc nên cư dân và đội kỹ thuật thực địa chịu ảnh hưởng trực tiếp |
# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)
```
┌─ QUICK PROBLEM CARD #1 ─────────────────────────────────────┐
│ Bài toán (1 câu): Nhân viên CSKH xử lý tay các ticket lặp   │
│   (thất lạc đồ, sai cước, tranh chấp thu nhập tài xế) dù    │
│   phần lớn có quy tắc giải quyết rõ ràng.                   │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác: ______           │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH (quá tải ticket), tài   │
│   xế và khách hàng (chờ phản hồi lâu).                      │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Nhận ticket ──> 2. Phân loại thủ công ──> 3. Tra cứu   │
│      chuyến đi/GPS/giao dịch ──> 4. Soạn và gửi phản hồi    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3, tra cứu chéo nhiều │
│   hệ thống (⏱ ~4-6 phút/lượt, tổng ticket ~6-10 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (tự phân       │
│   loại), bước 3 (tự truy xuất và đối chiếu dữ liệu), bước 4 │
│   (soạn phản hồi).                                          │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian xử lý  │
│   trung bình từ ~8 phút ──> dưới 2 phút; tự giải quyết hoàn │
│   toàn ≥ 50% ticket nhóm lặp.                               │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```
```
┌─ QUICK PROBLEM CARD #2 ─────────────────────────────────────┐
│ Bài toán (1 câu): Chuyên viên kiểm tra tay hồ sơ pháp lý,   │
│   hợp đồng và lịch thanh toán khi mở bán, mỗi hồ sơ tốn     │
│   nhiều thời gian và dễ sai sót phải làm lại.               │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác: ______           │
│                                                             │
│ Ai đang đau (Actor)? Chuyên viên pháp lý/kinh doanh xử lý   │
│   hồ sơ, và khách mua nhà chờ ký hợp đồng.                  │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Nhận hồ sơ ──> 2. Kiểm tra giấy tờ pháp lý khách hàng  │
│      ──> 3. Đối chiếu điều khoản hợp đồng và lịch thanh     │
│      toán ──> 4. Yêu cầu bổ sung/sửa ──> 5. Duyệt           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3, đối chiếu điều     │
│   khoản và số liệu (⏱ ~20-30 phút/lượt, tổng 30-60 phút/hồ  │
│   sơ)                                                       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (OCR và trích  │
│   xuất trường dữ liệu), bước 3 (đối chiếu và gắn cờ điểm    │
│   bất thường).                                              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian soát   │
│   xét từ ~45 phút ──> dưới 15 phút/hồ sơ; giảm tỷ lệ hồ sơ  │
│   phải làm lại từ 5-10% ──> dưới 2%.                        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
```
┌─ QUICK PROBLEM CARD #3 ─────────────────────────────────────┐
│ Bài toán (1 câu): Kỹ thuật viên tại xưởng dịch vụ chẩn đoán │
│   lỗi và tra cứu tài liệu kỹ thuật bằng tay, tỷ lệ sửa đúng │
│   ngay lần đầu thấp nên khách phải quay lại xưởng nhiều     │
│   lần.                                                      │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác: ______           │
│                                                             │
│ Ai đang đau (Actor)? Chủ xe VinFast (mất thời gian, bực bội │
│   khi quay lại xưởng), kỹ thuật viên và cố vấn dịch vụ.     │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Tiếp nhận xe và mô tả lỗi ──> 2. Đọc mã lỗi (DTC) và   │
│      log ──> 3. Tra tài liệu kỹ thuật/lịch sử sửa chữa ──>  │
│      4. Sửa chữa ──> 5. Kiểm tra lại                        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3, tra cứu thủ công   │
│   dẫn tới chẩn đoán sai (⏱ ~15-25 phút/lượt)                │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3: gợi ý       │
│   nguyên nhân gốc và quy trình sửa dựa trên mã lỗi, log và  │
│   tài liệu kỹ thuật.                                        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Tăng tỷ lệ sửa đúng   │
│   ngay lần đầu từ ~80% ──> trên 90%; giảm thời gian chẩn    │
│   đoán từ ~20 phút ──> dưới 8 phút.                         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
│ (LLM + RAG trên tài liệu kỹ thuật và lịch sử sửa chữa)      │
└─────────────────────────────────────────────────────────────┘
```