Ý tưởng chính: Tái sử dụng (share) những phần dữ liệu nội dung chung giữa nhiều object để tiết kiệm bộ nhớ; giữ phần “state” chia sẻ vs phần “state” riêng biệt.
Cấu trúc:

Flyweight objects (shared intrinsic state) + External state do client cấp (extrinsic).

FlyweightFactory quản lý cache/đưa lại instance.
Khi dùng / ví dụ:

Khi cần nhiều object giống nhau (millions) như cây trong game, ký tự trong text editor.

Ví dụ đời sống: hàng chục ghế giống nhau trong quán, chỉ lưu 1 bản mô tả.
Triển khai nhanh / tip:

Tách data thành intrinsic (chung) và extrinsic (riêng). Lưu flyweights trong factory dict bằng key.
Ưu / Nhược:

Tiết kiệm RAM lớn; tăng performance khi tạo nhiều object.

− Phức tạp quản lý extrinsic state; code ít trực quan hơn.
1 câu giải thích: “Flyweight = dùng chung mẫu cho nhiều đối tượng, chỉ truyền khác biệt vào lúc cần.”