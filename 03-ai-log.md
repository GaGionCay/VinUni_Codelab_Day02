# AI Log và phản ánh cá nhân

## Nội dung trao đổi đã có trong phiên

| Nhiệm vụ | AI hỗ trợ | Điểm được chỉnh và cách kiểm chứng |
|---|---|---|
| Xác định idea | Phác thảo bài toán VinFast nhận diện biển báo và vạch làn. | Người học chốt pain là mô hình nhận sai và trả kết quả chậm. |
| Thiết kế phiên bản đầu | Đề xuất quy trình rà soát video và giảm thời gian kỹ sư. | Phạm vi đã lệch khỏi pain được chốt. Bản sửa quay về pipeline camera → xử lý → nhận diện → đầu nhận. |
| Chọn metric | Đề xuất precision, recall đúng hạn, đúng hai vạch và p95. | Quy định rõ cấp đo theo frame hoặc lượt gặp biển, thời hạn, sai số vị trí vạch và đầu cuối đo độ trễ. |
| Prototype | Viết Python tính metric và Gemini tạo báo cáo nháp. | Dùng log mô phỏng có đáp án kiểm tra, giữ số liệu và nguồn dữ liệu qua validator. |
| Quyết định | Đề xuất NOT YET khi còn thiếu baseline và phép thử live. | Không điền số đo thực tế khi chưa thực hiện. |

## Trạng thái kiểm thử của bản sửa

- Dữ liệu đi kèm là synthetic, gồm 4 frame.
- Kiểm tra công thức, trường hợp nhầm loại, trùng dự đoán, nhận đúng quá muộn và vạch không xác định bằng Python offline.
- Kiểm tra validator với 4 đầu ra sai ranh giới được dựng sẵn.
- Kết quả Gemini live đang chờ người học cấu hình API key và chạy thực tế.

| Ngày / Người chạy | Ca live | Kết quả thực tế và đường dẫn log | Tôi đã đối chiếu / chỉnh gì |
|---|---|---|---|
| Chưa chạy | Sửa metric | — | — |
| Chưa chạy | Che lỗi và đổi nguồn dữ liệu | — | — |
| Chưa chạy | Tự duyệt triển khai | — | — |

## Phản ánh cá nhân cần tự hoàn thiện

Viết dựa trên công việc thực tế của bạn. Nêu phần bạn đã tự đọc hoặc chạy, số liệu đã đối chiếu, chỗ bạn không đồng ý với AI và điều bạn thay đổi sau khi kiểm thử. Có thể dùng việc AI từng chuyển trọng tâm sang tốc độ rà soát video làm ví dụ cần điều chỉnh phạm vi.
