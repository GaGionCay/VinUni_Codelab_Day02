# Nhật ký Tương tác & Nhật ký AI (AI Assistance Log)

## 1. Tóm tắt sự hỗ trợ từ AI (AI Assistance Summary)

- **Brainstorm ý tưởng:** Nhờ AI gợi ý 5 bài toán thực tế phù hợp với hệ sinh thái các doanh nghiệp thuộc Vingroup (VinFast, Vinhomes, Vinmec, Vinpearl, VinAI/VinBus).
- **Xây dựng cấu trúc:** AI hỗ trợ định hình và chuẩn hóa các trường thông tin cho Thẻ Vấn Đề (Problem Cards), Phát biểu bài toán 6 trường và Bảng kiểm độ sẵn sàng (Readiness Checklist).
- **Lập trình / Debug:** AI hỗ trợ viết script Python kiểm tra kết nối API và xử lý các lỗi kỹ thuật phát sinh trong quá trình thử nghiệm.

---

## 2. Ghi nhận lỗi và hiện tượng ảo giác của AI (Hallucination & Errors)

- **Sự cố thực tế đã gặp:** Khi tiến hành cấu hình gọi Gemini API bằng Python trong quá trình làm bài, đoạn code test ban đầu gặp lỗi:  
  `404 NOT_FOUND: This model models/gemini-2.5-flash is no longer available to new users...`
- **Nguyên nhân:** AI hoặc tài liệu tham khảo cũ đề xuất sử dụng phiên bản model không còn khả dụng cho các API key mới tạo.

---

## 3. Cách tinh chỉnh Prompt và Thiết lập giới hạn (Prompt Refinement & Boundaries)

- **Cách khắc phục:** Cung cấp ngược lại thông báo lỗi chi tiết cho AI để yêu cầu AI cập nhật tên model mới chính xác (`gemini-3.8-flash`).
- **Thiết lập giới hạn (Boundaries) khi làm việc với AI:**
  - **Bảo mật:** Yêu cầu AI tuân thủ nguyên tắc bảo mật: Tuyệt đối không mã hóa cứng (*hardcode*) API key vào trong source code Python mà phải sử dụng biến môi trường (`os.getenv`).
  - **Chất lượng nội dung:** Kiểm soát các nội dung phân tích bài toán Vingroup để đảm bảo tính logic, có số liệu định lượng hợp lý thay vì đưa ra các con số chung chung.