Nguyên lý đời thường:

Tạo object phức tạp bằng cách lắp ghép từng phần.

Ví dụ: Làm burger: cho bánh → thêm thịt → thêm phô mai → thêm sốt → ra chiếc burger custom.

Nguyên lý trong code:

Object phức tạp (Burger, House, Report) được tạo dần qua nhiều bước nhỏ (add_part).

Giúp dễ dàng tùy chỉnh từng phần mà không cần viết 100 constructor khác nhau.

Dùng khi: Object có nhiều tham số tùy chọn, hoặc phải tạo theo từng bước.