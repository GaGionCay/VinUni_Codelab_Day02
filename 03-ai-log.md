# AI INTERACTION LOG

## 1. Tổng quan quá trình tương tác

Trong Lab 02, tôi sử dụng AI để hỗ trợ phân tích bài toán tiếp nhận và xử lý yêu cầu thay đổi người đón hoặc lịch xe buýt của học sinh tại Vinschool.

Ban đầu, tôi mới xác định được vấn đề ở mức tổng quát: phụ huynh gửi yêu cầu qua nhiều kênh, khiến nhân viên phải tiếp nhận và kiểm tra thông tin thủ công. Tuy nhiên, tôi chưa làm rõ được các bước nghiệp vụ, những thông tin cần xác minh và phạm vi AI có thể tham gia.

Quá trình tương tác tập trung vào việc làm rõ bài toán, xây dựng workflow, xác định vai trò của AI, đề xuất cách đánh giá và hoàn thiện báo cáo.

## 2. AI đã giúp ích gì cho tôi?

- **Làm rõ bài toán:** AI giúp tôi chuyển vấn đề ban đầu thành một bài toán cụ thể hơn: hỗ trợ tiếp nhận, trích xuất và đối chiếu yêu cầu thay đổi thông tin đón học sinh.
- **Hiểu rõ nghiệp vụ:** Qua trao đổi, tôi xác định được những thông tin cần xử lý như học sinh, ngày áp dụng, người được đề nghị đón và tuyến xe buýt. Tôi cũng hiểu rằng trích xuất đủ thông tin không đồng nghĩa với việc yêu cầu đã được xác minh hoặc phê duyệt.
- **Xây dựng workflow:** AI hỗ trợ tôi sắp xếp lại quy trình theo trình tự: tiếp nhận yêu cầu → xác định học sinh → trích xuất nội dung thay đổi → kiểm tra thông tin → chuyển nhân viên xác nhận.
- **Xác định vai trò của AI:** AI giúp tôi phân biệt công việc của LLM và xử lý bằng quy tắc. LLM phù hợp để đọc yêu cầu và trích xuất thông tin; Python hỗ trợ kiểm tra dữ liệu thiếu hoặc mâu thuẫn. Nhân viên vẫn là người quyết định cuối cùng.
- **Hoàn thiện báo cáo:** AI hỗ trợ chỉnh sửa câu từ, chuẩn hóa thuật ngữ chuyên ngành và rà soát tính nhất quán giữa problem statement, workflow, metric và giải pháp đề xuất.

## 3. Những điểm tôi phải điều chỉnh trong đề xuất của AI

### a. Làm rõ nghiệp vụ thay vì chỉ tập trung vào xử lý văn bản

Ban đầu, đề xuất của AI chủ yếu tập trung vào việc đọc và phân loại yêu cầu của phụ huynh. Tôi điều chỉnh để bài toán bao quát cả việc xác định học sinh, ngày áp dụng, nội dung thay đổi và tình trạng xác minh. Nhờ đó, giải pháp không chỉ dừng ở một chatbot trích xuất thông tin.

### b. Điều chỉnh workflow và phạm vi AI

Tôi yêu cầu tách riêng các bước trích xuất, kiểm tra và xác nhận thay vì gộp thành một công đoạn. Đặc biệt, AI không được tự phê duyệt người đón hoặc cập nhật thông tin khi chưa có xác nhận của nhân viên. Những yêu cầu thiếu thông tin hoặc có mâu thuẫn phải được chuyển sang trạng thái cần xem xét.

### c. Phân biệt đề xuất với kết quả thực tế

Một số nội dung về quy trình nội bộ của Vinschool chưa có tài liệu xác nhận. Vì vậy, tôi giữ chúng ở mức giả định phục vụ phân tích, không trình bày như quy trình chính thức. Tương tự, các metric trong báo cáo là mục tiêu đề xuất, chưa phải kết quả đo thực tế.

## 4. Cách tôi định hướng giải pháp và kiểm soát đầu ra

Qua quá trình trao đổi, tôi xác định giải pháp nên kết hợp ba thành phần:

1. **LLM:** Đọc yêu cầu và trích xuất thông tin thành cấu trúc dữ liệu.
2. **Python/Rule:** Kiểm tra trường thông tin bắt buộc, phát hiện dữ liệu thiếu hoặc mâu thuẫn.
3. **Human-in-the-loop:** Nhân viên xem xét và xác nhận trước khi thực hiện thay đổi.

Tôi cũng xác định một số tình huống cần kiểm tra trong prototype như thiếu thông tin học sinh, thông tin người đón không khớp, yêu cầu AI tự phê duyệt hoặc yêu cầu khẩn cấp nhưng chưa được xác minh.

Các trường hợp này giúp kiểm tra liệu hệ thống có giữ đúng giới hạn hay không. Prototype cần sử dụng dữ liệu giả lập, không sử dụng thông tin cá nhân thật của học sinh và phụ huynh.

## 5. Bài học cá nhân rút ra

Qua quá trình làm việc, tôi nhận ra rằng cần hiểu rõ nghiệp vụ trước khi đề xuất ứng dụng AI. Ban đầu, tôi nhìn vấn đề chủ yếu từ góc độ xử lý văn bản, nhưng sau khi phân tích workflow, tôi hiểu rằng bài toán còn liên quan đến đối chiếu dữ liệu, xác minh thông tin và trách nhiệm của nhân viên.

Tôi cũng học được cách sử dụng AI để hỗ trợ phân tích và phản biện thay vì tiếp nhận nguyên văn các đề xuất. Một giải pháp có vẻ hợp lý về mặt kỹ thuật vẫn có thể không phù hợp nếu giải quyết sai vấn đề hoặc bỏ qua bước nghiệp vụ quan trọng.

Ngoài ra, AI giúp tôi cải thiện cách trình bày báo cáo theo hướng rõ ràng, có cấu trúc và sử dụng thuật ngữ chuyên ngành phù hợp hơn. Tuy nhiên, tôi vẫn cần kiểm tra tính chính xác của nội dung và phân biệt rõ giữa giả định, đề xuất và kết quả đã được kiểm chứng.

Hiện tại, giải pháp Vinschool mới dừng ở mức đề xuất và prototype thử nghiệm. Tôi giữ quyết định **NOT YET** đối với triển khai thực tế do chưa có dữ liệu vận hành và kết quả đánh giá trên hệ thống thật. Bước tiếp theo là xây dựng bộ dữ liệu giả lập có nhãn để kiểm tra độ chính xác trích xuất, khả năng phát hiện yêu cầu cần xác minh và thời gian xử lý.
