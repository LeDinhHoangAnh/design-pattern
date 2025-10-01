Ý tưởng chính: Tách abstraction (khái niệm) ra khỏi implementation để hai bên thay đổi độc lập.
Cấu trúc:

Abstraction (interface cao cấp) có tham chiếu tới Implementor (interface cho implement cụ thể).

ConcreteAbstraction ↔ ConcreteImplementor(s).
Khi dùng / ví dụ:

Khi có hai chiều biến hóa độc lập: ví dụ Shapes (Circle, Square) × Renderer (SVG, Canvas).

Ví dụ đời sống: hình (tròn/vuông) và màu (đỏ/xanh) — bạn muốn tự do kết hợp.
Triển khai nhanh / tip:

Định nghĩa interface Implementor (ví dụ Renderer.render_circle()), Abstraction gọi methods này.
Ưu / Nhược:

Giảm comb explosion (m×n). Thay đổi implementor không ảnh hưởng abstraction.

− Thêm lớp phức tạp hơn.
1 câu giải thích: “Bridge tách 2 phần để bạn có thể mix-and-match dễ dàng.”