import socket

HOST = "127.0.0.1"
PORT = 8900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"Hello, world")
data = s.recv(1024)

print("Received: ", data.decode())
s.close()
