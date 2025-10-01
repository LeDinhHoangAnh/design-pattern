Ý tưởng chính: Đối xử đồng nhất giữa đối tượng đơn lẻ (leaf) và tập hợp (composite) bằng cùng interface.
Cấu trúc:

Component (interface) ← Leaf (đơn), Composite (chứa list<Component>)
Khi dùng / ví dụ:

Cây thư mục: File (leaf) và Folder (composite). GUI tree, menu, scene-graph game.
Triển khai nhanh / tip:

Component có các method chung (render(), get_size()); Composite implement bằng vòng lặp gọi child.method().
Ưu / Nhược:

Dễ quản lý cấu trúc phân cấp, client code đơn giản (đệ quy).

− Quản lý lifecycle/limit recursion cần chú ý.
1 câu giải thích: “Composite cho phép dùng 1 interface cho 1 món hoặc cả rổ món.”