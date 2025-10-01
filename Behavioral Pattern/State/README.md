Ý tưởng: Biến đổi hành vi của một đối tượng khi trạng thái bên trong thay đổi.

Cấu trúc:

State: interface các hành vi.

ConcreteState: định nghĩa hành vi theo từng trạng thái.

Context: chứa trạng thái hiện tại.

Áp dụng khi:

Một đối tượng có nhiều trạng thái khác nhau, hành vi thay đổi theo trạng thái.

Ví dụ đời thường: Máy bán nước: khi có tiền thì cho lấy nước, khi hết nước thì báo lỗi.