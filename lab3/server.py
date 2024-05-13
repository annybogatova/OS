import socket
import threading

def handle_client(conn, addr):
    print(f"Новое соединение: {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            modified_data = f"Server: {data.decode()}"

            conn.sendall(modified_data.encode())

    finally:
        conn.close()
        print(f"Соединение с {addr} закрыто")

if __name__ == "__main__":

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 8000)
	server_socket.bind(server_address)
	server_socket.listen(5)

	print(f"Сервер запущен на {server_address}")

	while True:
		print('Ожидание соединений...')
		conn, addr = server_socket.accept()
		client_thread = threading.Thread(target=handle_client, args=(conn, addr))

		client_thread.start()
