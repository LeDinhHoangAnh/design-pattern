Nguyên lý đời thường:

Bạn không trực tiếp “nặn” object → mà nhờ 1 nhà máy chung (Factory) lo tạo.

Ví dụ: Bạn vào quán cafe, chỉ cần gọi “Latte” → quán sẽ đưa bạn 1 cốc Latte đúng chuẩn.

Nguyên lý trong code:

Khi muốn tạo object, bạn gọi factory.create(type) thay vì new Latte().

Nhờ đó, thay đổi logic tạo object chỉ ở 1 chỗ, không ảnh hưởng các nơi khác.

Dùng khi: Bạn có nhiều loại object cùng họ (Coffee, Tea, Juice…).