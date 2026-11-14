
import socket
import os

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is waiting for connection...")

conn, addr = server_socket.accept()

with conn:
    print("Connected by:", addr)

    filename = conn.recv(1024).decode()

    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            content = f.read()

        conn.sendall(content.encode())
    else:
        conn.sendall(b"File not found.")

server_socket.close()
