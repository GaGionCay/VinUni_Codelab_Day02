import os
import sys
from google import genai

# Lấy API key từ biến môi trường đã thiết lập
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Lỗi: Biến môi trường GEMINI_API_KEY chưa được thiết lập!")
    sys.exit(1)
else:
    print("Đã nhận diện được API Key. Đang kiểm tra kết nối...")
    
    # Khởi tạo client theo chuẩn mới của Google GenAI SDK
    client = genai.Client()
    
    try:
        # Thử gọi một mô hình đơn giản để test
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="Xin chào, hãy trả lời ngắn gọn: Bạn là ai?",
        )
        print("Kết nối thành công! Phản hồi từ mô hình:")
        print(response.text)
    except Exception as e:
        print(f"Kết nối thất bại, vui lòng kiểm tra lại key. Lỗi: {e}")
        sys.exit(1)