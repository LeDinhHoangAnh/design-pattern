Ý tưởng chính: Một object đứng giữa client và real subject để kiểm soát / tối ưu truy cập (bảo mật, lazy loading, logging, caching).
Cấu trúc:

Client → Proxy (cùng interface) → RealSubject.
Các loại proxy phổ biến:

Remote proxy (proxy tới object ở nơi khác), Virtual proxy (tạo real object chậm khi cần), Protection proxy (kiểm quyền), Caching proxy.
Khi dùng / ví dụ:

Khi muốn kiểm soát quyền truy cập, lazy-load big object, hoặc cache kết quả.

Ví dụ đời sống: thuê luật sư đại diện (proxy) xử lý thay bạn.
Triển khai nhanh / tip:

Proxy implement cùng interface, giữ reference tới real subject; thêm logic trước/after gọi real.
Ưu / Nhược:

Kiểm soát, bảo mật, lazy-init, caching.

− Có thêm lớp trung gian, overhead thời gian/độ phức tạp.
1 câu giải thích: “Proxy = người đại diện, đứng ra kiểm soát và tối ưu cho object thật.”