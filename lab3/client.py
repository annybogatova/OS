import socket

if __name__ == '__main__':
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = ('localhost', 8000)
	client_socket.connect(server_address)

	try:
		while True:
			message = input("Введите сообщение: ")

			client_socket.sendall(message.encode())

			data = client_socket.recv(1024)

			print('Полученные данные:', data.decode())

	finally:
		client_socket.close()
