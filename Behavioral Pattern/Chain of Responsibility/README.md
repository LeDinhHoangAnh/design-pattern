Ý tưởng: Thay vì 1 đối tượng xử lý tất cả yêu cầu, ta sắp xếp nhiều “người xử lý” thành một chuỗi. Yêu cầu được chuyển qua từng người cho đến khi có người xử lý được.

Cấu trúc:

Handler: interface chung có handle(request)

ConcreteHandler: mỗi “người xử lý” sẽ quyết định có xử lý không, nếu không thì chuyển tiếp cho người sau.

Client: gửi request vào chuỗi.

Áp dụng khi:

Có nhiều khả năng xử lý khác nhau cho một yêu cầu.

Muốn tách rời client khỏi logic quyết định ai xử lý.

Ví dụ đời thường: Xin nghỉ phép: leader → manager → giám đốc.