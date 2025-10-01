Nguyên lý đời thường:

Tạo object mới bằng cách nhân bản từ 1 mẫu có sẵn.

Ví dụ: Bạn có file Word template → copy ra → sửa chút → thành file mới.

Nguyên lý trong code:

Dùng copy() hoặc clone() để tạo bản sao từ object gốc.

Nhanh hơn nhiều so với việc khởi tạo lại từ đầu.

Dùng khi: Object phức tạp, tốn kém khi tạo mới (ví dụ: object đã load dữ liệu nặng).