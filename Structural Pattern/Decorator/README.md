Ý tưởng chính: Thêm hành vi/khả năng cho object tại runtime, bằng cách “bọc” object bằng wrapper có cùng interface.
Cấu trúc:

Component (interface) ← ConcreteComponent

Decorator implements Component và giữ tham chiếu tới Component (wrap).
Khi dùng / ví dụ:

Thêm logging, caching, validation cho service; GUI: thêm border/scroll.

Ví dụ đời sống: pizza cơ bản → bọc thêm cheese, bọc thêm pepperoni.
Triển khai nhanh / tip:

Viết lớp Decorator có method gọi component.method() trước/sau để thêm logic. Trong Python có thể dùng function decorator.
Ưu / Nhược:

Thêm chức năng linh hoạt, stackable.

− Có thể tạo nhiều wrapper chồng lên nhau khó debug.
1 câu giải thích: “Decorator = topping; bạn bọc thêm tính năng mà không sửa class gốc.”