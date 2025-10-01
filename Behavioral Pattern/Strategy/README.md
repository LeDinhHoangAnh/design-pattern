Ý tưởng: Đóng gói nhiều thuật toán khác nhau và cho phép lựa chọn 1 thuật toán tại runtime.

Cấu trúc:

Strategy: interface chung.

ConcreteStrategy: các thuật toán cụ thể.

Context: sử dụng một strategy.

Áp dụng khi:

Có nhiều cách giải quyết cùng 1 vấn đề và muốn dễ dàng thay đổi.

Ví dụ đời thường: Ứng dụng gọi xe: chọn đi xe máy, ô tô, hoặc taxi.