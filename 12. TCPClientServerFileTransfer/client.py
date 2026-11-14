
import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

filename = input("Enter file name to request: ")

client_socket.sendall(filename.encode())

data = client_socket.recv(4096).decode()

print("\n--- File Content ---")
print(data)

client_socket.close()
