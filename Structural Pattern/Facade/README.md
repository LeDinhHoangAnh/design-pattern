Ý tưởng chính: Đơn giản hóa API phức tạp bằng 1 interface cao cấp (một điểm gọi duy nhất).
Cấu trúc:

Client → Facade → nhiều Subsystem objects.
Khi dùng / ví dụ:

Khi hệ thống có nhiều service/phases (DB, cache, queue, payment) → expose 1 method process_order() thay vì bắt client gọi từng service.

Ví dụ đời sống: lễ tân khách sạn lo tất cả thủ tục cho bạn.
Triển khai nhanh / tip:

Viết Facade class gom các thao tác tuần tự, xử lý lỗi chung, trả kết quả đơn giản.
Ưu / Nhược:

Giảm coupling, dễ dùng cho client.

− Có thể che dấu chi tiết cần debug; tránh đặt logic quá nhiều vào facade.
1 câu giải thích: “Facade = lễ tân, gọi 1 nơi giải quyết nhiều việc phức tạp phía sau.”