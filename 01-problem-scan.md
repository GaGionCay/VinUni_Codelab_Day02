Báo cáo Quét Vấn đề (Problem Scan) — Vingroup
1. Danh sách 5 Vấn đề Thực tế tại Vingroup

1. VinFast: Tối ưu thời gian phản hồi/kiểm tra lỗi bảo hành hệ thống pin xe điện.
2. Vinhomes: Xử lý và phân loại tự động hàng nghìn phản ánh cư dân qua app cư dân mỗi ngày.
3. Vinmec: Tự động trích xuất thông tin bệnh án và đề xuất tóm tắt tiền sử cho bác sĩ trước ca khám.
4. Vinpearl: Dự báo nhu cầu đặt phòng và cá nhân hóa lịch trình trải nghiệm cho khách lưu trú.
5. VinAI / VinBus: Quản lý và phân tích dữ liệu camera hành trình tự động để cảnh báo an toàn tài xế.

2. Phân loại theo 4 lăng kính (Four Lenses)
1. Business Value (Giá trị kinh doanh): Mức độ ảnh hưởng đến chi phí, doanh thu, năng suất và hiệu quả vận hành.
2. Customer / User Impact (Tác động đến khách hàng/người dùng): Mức độ cải thiện trải nghiệm, tốc độ phản hồi, chất lượng dịch vụ và an toàn.
3. Technical Feasibility (Tính khả thi kỹ thuật): Mức độ phù hợp của công nghệ AI, độ phức tạp tích hợp và khả năng triển khai thử nghiệm.
4. Data & Operational Readiness (Mức độ sẵn sàng dữ liệu và vận hành): Khả năng tiếp cận dữ liệu, chất lượng dữ liệu, quy trình và con người cần thiết.

Vấn đề	Lăng kính nổi bật
VinFast – Bảo hành pin xe điện	Technical Feasibility; Data & Operational Readiness
Vinhomes – Phân loại phản ánh cư dân	Customer / User Impact; Business Value
Vinmec – Tóm tắt bệnh án	Customer / User Impact; Data & Operational Readiness
Vinpearl – Dự báo nhu cầu và cá nhân hóa	Business Value; Customer / User Impact
VinAI / VinBus – Cảnh báo an toàn	Customer / User Impact; Technical Feasibility


Top 3 vấn đề xuất ưu tiên:
Ba vấn đề được đề xuất ưu tiên đánh giá sâu hơn:
1. Vinhomes – Phân loại tự động phản ánh cư dân: Bài toán văn bản có quy trình đầu vào/đầu ra tương đối rõ; có thể giới hạn PoC ở phân loại và định tuyến, đồng thời giữ human review cho trường hợp rủi ro.
2. Vinpearl – Dự báo nhu cầu dịch vụ: Có thể bắt đầu bằng một phạm vi dự báo hẹp, chẳng hạn nhu cầu F&B, rồi đánh giá sai số trên dữ liệu lịch sử trước khi mở rộng sang cá nhân hóa.
3. Vinmec – Tóm tắt bệnh án: Có thể định vị AI như công cụ hỗ trợ tổng hợp thông tin cho bác sĩ, không thay thế quyết định chuyên môn; cần kiểm tra chặt chẽ quyền truy cập, bảo mật và chất lượng dữ liệu y tế.

3. Thẻ Vấn đề Chi tiết (Problem Cards)

Thẻ Vấn đề 1: Phân loại tự động phản ánh cư dân Vinhomes 
- Tác nhân (Actor): Bộ phận Chăm sóc Khách hàng (CSKH) & Ban quản lý (BQL) Vinhomes.
- Quy trình hiện tại (Current Process): Cư dân gửi ticket qua app -> Nhân viên đọc từng ticket thủ công -> Phân loại thủ công vào từng phòng ban (Điện, Nước, Dịch vụ, An ninh) -> Chuyển giao công việc.
- Điểm nghẽn (Bottleneck): Quá tải vào giờ cao điểm khiến quá trình tiếp nhận, đọc hiểu, phân loại và định tuyến ticket bị kéo dài. Theo các mốc thời gian ước tính trong quy trình hiện tại, tổng thời gian từ lúc cư dân gửi ticket đến khi bộ phận chuyên trách tiếp nhận khoảng 1 giờ 20 phút – 2 giờ 37 phút. Tỷ lệ phân loại sai phòng ban ước tính khoảng 15–20%, có thể dẫn đến chuyển nhầm hoặc đùn đẩy công việc.
- Giải pháp AI (AI Solution): Sử dụng LLM Text Classification & Intent Analysis tự động phân tích phản ánh, gán nhãn mức độ ưu tiên và tự động routing (chuyển tiếp) chính xác đến bộ phận xử lý tương ứng.
- Chỉ số đo lường (Metric):
  - Giảm thời gian định tuyến tự động xuống dưới 2 phút đối với ticket có confidence score ≥ 85% và không thuộc nhóm nhạy cảm.
  - Tăng độ chính xác phân loại tự động lên trên 90% đối với nhóm ticket đủ điều kiện tự động định tuyến.
  - Tăng mức độ hài lòng của cư dân (CSAT) lên 15%.


Thẻ Vấn đề 2: Tối ưu kiểm tra & bảo hành pin xe điện VinFast
- Tác nhân (Actor): Kỹ thuật viên Xưởng dịch vụ (Service Center) & Đội ngũ R&D VinFast.
- Quy trình hiện tại (Current Process): Xe vào xưởng -> Kỹ thuật viên cắm thiết bị đọc dữ liệu telemetry/BMS -> Đọc mã lỗi (DTC) & kiểm tra các thông số pin thủ công -> Đánh giá phương án thay thế/sửa chữa.
- Điểm nghẽn (Bottleneck): Thời gian chẩn đoán kéo dài (từ vài giờ đến vài ngày với các lỗi ẩn/chập chập); dữ liệu pin lớn nhưng chưa khai thác tối đa để phát hiện sớm nguy cơ trước khi xảy ra sự cố.
- Giải pháp AI (AI Solution): Predictive Maintenance & Anomaly Detection model trên dữ liệu BMS/Telemetry từ Cloud để phát hiện bất thường tế bào pin (cell anomaly) trước khi lỗi xảy ra và đề xuất phương án xử lý nhanh cho kỹ thuật viên.
- Chỉ số đo lường (Metric):
  - Giảm thời gian chẩn đoán lỗi pin tại xưởng từ 3 tiếng xuống < 30 phút.
  - Dự báo sớm 80% nguy cơ hỏng hóc pin trước 48 giờ.

Thẻ Vấn đề 3: Tóm tắt bệnh án & tiền sử y khoa tự động tại Vinmec
- Tác nhân (Actor): Bác sĩ khám bệnh & Đội ngũ Y tá tại Bệnh viện Vinmec.
- Quy trình hiện tại (Current Process): Bác sĩ mở hồ sơ bệnh án điện tử (EMR) -> Đọc thủ công hàng chục trang lịch sử khám, kết quả xét nghiệm, đơn thuốc cũ -> Tổng hợp thông tin trong 3-5 phút trước khi bắt đầu tư vấn.
- Điểm nghẽn (Bottleneck): Áp lực thời gian mỗi ca khám (chỉ có 10–15 phút/bệnh nhân); dễ bỏ sót các chi tiết tiền sử quan trọng (dị ứng thuốc, bệnh nền phức tạp) nằm rải rác trong tài liệu cũ.
- Giải pháp AI (AI Solution): Sử dụng Medical RAG + LLM Summarization tích hợp EMR để trích xuất, tổng hợp ngắn gọn tiền sử bệnh, dị ứng và các chỉ số xét nghiệm bất thường thành một bản tóm tắt 1 trang cho bác sĩ trước khi bệnh nhân vào phòng khám.
- Chỉ số đo lường (Metric):
  - Giảm thời gian đọc và chuẩn bị hồ sơ từ 5 phút xuống < 1 phút/ca.
  - Giảm 95% rủi ro bỏ sót thông tin chống chỉ định thuốc/dị ứng của bệnh nhân.

Thẻ Vấn đề 4: Cá nhân hóa trải nghiệm & dự báo nhu cầu dịch vụ Vinpearl
- Tác nhân (Actor): Bộ phận Lễ tân, F&B và Quản lý Vận hành Vinpearl.
- Quy trình hiện tại (Current Process): Lập kế hoạch công suất phục vụ dựa trên kinh nghiệm quá khứ -> Khuyến nghị lịch trình tham quan/ăn uống cho khách theo gói tour cố định.
- Điểm nghẽn (Bottleneck): Đã xảy ra tình trạng lãng phí nguyên vật liệu F&B hoặc thiếu hụt nhân sự giờ cao điểm; gợi ý dịch vụ chưa thực sự cá nhân hóa theo sở thích từng gia đình/khách lẻ.
- Giải pháp AI (AI Solution): Time-series Forecasting (dự báo lượng khách & nhu cầu sử dụng dịch vụ) kết hợp Recommendation System tạo lịch trình trải nghiệm (gợi ý nhà hàng, thời gian đi VinWonders, dịch vụ Spa) riêng biệt cho từng khách hàng qua app Vinpearl.
- Chỉ số đo lường (Metric):
  - Sai số dự báo nhu cầu F&B/nguyên liệu giảm từ 20% xuống < 7%.
  - Tăng doanh thu bán chéo dịch vụ (Cross-selling/Up-selling) thêm 12%.

Thẻ Vấn đề 5: Phân tích camera hành trình & cảnh báo an toàn VinAI / VinBus
- Tác nhân (Actor): Tài xế xe buýt điện VinBus & Đội ngũ giám sát an toàn giao thông.
- Quy trình hiện tại (Current Process): Camera ghi hình liên tục -> Dữ liệu lưu vào ổ cứng -> Khi xảy ra sự cố hoặc va chạm mới trích xuất video để kiểm tra lại hậu kỳ.
- Điểm nghẽn (Bottleneck): Không cảnh báo kịp thời các hành vi rủi ro tức thì (tài xế ngủ gật, mất tập trung, dùng điện thoại, khoảng cách an toàn không đảm bảo) ngay tại thời điểm lái xe.
- Giải pháp AI (AI Solution): Đưa mô hình Computer Vision (Driver Monitoring System - DMS & ADAS) chạy trực tiếp tại vi xử lý Edge AI trên xe, phân tích luồng video real-time để phát cảnh báo âm thanh/rung ghế tức thì cho tài xế và gửi dữ liệu sự cố về trung tâm điều hành.
- Chỉ số đo lường (Metric):
  - Thời gian cảnh báo phản hồi dưới 300ms ngay khi phát hiện hành vi nguy hiểm.
  - Giảm 40% các vi phạm an toàn lái xe và nguy cơ va chạm giao thông.