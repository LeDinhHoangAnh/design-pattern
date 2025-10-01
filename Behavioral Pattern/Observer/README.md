Ý tưởng: Một đối tượng (Subject) có nhiều người theo dõi (Observers). Khi Subject thay đổi, nó sẽ tự động thông báo cho Observers.

Cấu trúc:

Subject: có danh sách observers và hàm notify().

Observer: có hàm update().

Áp dụng khi:

Muốn tự động cập nhật nhiều nơi khi dữ liệu thay đổi.

Ví dụ đời thường: Đăng ký kênh YouTube → có video mới thì nhận thông báo.