import ssl
import socket
import threading

# Thông tin server
server_address = ("localhost", 12345)

# Danh sách các client đã kết nối
clients = []

# Hàm xử lý client
def handle_client(client_socket):
    print("Đã kết nối với:", client_socket.getpeername())
    clients.append(client_socket)

    try:
        # Nhận và gửi dữ liệu
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))
            
            # Gửi dữ liệu tới các client khác
            for client in clients:
                if client != client_socket:
                    client.send(data)
    except:
        pass
    finally:
        clients.remove(client_socket)
        print("Đã ngắt kết nối với:", client_socket.getpeername())
        client_socket.close()

# Tạo socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server đang lắng nghe...")

# Vòng lặp chờ kết nối
while True:
    client_socket, client_address = server_socket.accept()
    print("Kết nối từ:", client_address)

    # Tạo SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="certificates/server-cert.crt", keyfile="certificates/server-key.key")

    # Bọc socket bằng SSL
    client_socket = context.wrap_socket(client_socket, server_side=True)

    # Tạo luồng xử lý client
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
