Ý tưởng: Đóng gói một hành động (command) thành một đối tượng → dễ dàng truyền đi, lưu lại, undo/redo.

Cấu trúc:

Command: interface có execute().

ConcreteCommand: triển khai execute() (ví dụ: bật đèn, tắt đèn).

Invoker: người gọi lệnh (ví dụ: remote).

Receiver: đối tượng thực sự thực hiện (ví dụ: cái đèn).

Áp dụng khi:

Cần undo/redo hành động.

Muốn xếp hàng đợi (queue) các lệnh.

Ví dụ đời thường: Remote TV lưu lệnh “bật, tắt, chuyển kênh” và có thể undo.