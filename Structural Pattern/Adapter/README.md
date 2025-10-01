Ý tưởng: Adapter ví như một bộ chuyển đổi để hai interface không tương thích có thể làm việc được với nhau
Cấu trúc:

Client → Target (interface mong muốn) ← Adapter → Adaptee (interface cũ).
Khi dùng / ví dụ:

Khi bạn reuse thư viện cũ (Adaptee) nhưng muốn client gọi theo API mới (Target).

Ví dụ đời sống: ổ cắm 3 chấu ↔ 2 chấu (adapter chuyển đổi).
Triển khai nhanh / tip:

Viết lớp Adapter cài interface Target, bên trong gọi Adaptee.
Ưu / Nhược:

Giữ code client sạch, tái sử dụng legacy.

− Thêm lớp trung gian, có thể che dấu sai thiết kế nếu lạm dụng.
1 câu giải thích: “Adapter = ổ cắm chuyển đổi để hai thứ không khớp vẫn kết nối được.”