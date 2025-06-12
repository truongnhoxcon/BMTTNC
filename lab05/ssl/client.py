import ssl
import socket
import threading

# Thông tin server
server_address = ("localhost", 12345)

# Hàm nhận dữ liệu
def receive_data(ssl_socket):
    while True:
        try:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))
        except:
            ssl_socket.close()
            print("Kết nối đã đóng.")
            break

# Tạo socket thường
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # Nếu muốn bảo mật hơn, bạn nên dùng CERT_REQUIRED và cung cấp cert của server

# Bọc socket bằng SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Kết nối đến server
ssl_socket.connect(server_address)

# Tạo thread để nhận dữ liệu
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu
try:
    while True:
        msg = input("Nhập nội dung: ")
        ssl_socket.send(msg.encode("utf-8"))
except KeyboardInterrupt:
    print("Ngắt kết nối.")
finally:
    ssl_socket.close()
