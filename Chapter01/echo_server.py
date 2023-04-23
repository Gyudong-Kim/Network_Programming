import socket

HOST = ""
PORT = 8900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Server start !!")
conn, addr = s.accept()
print("Connected by", addr)

try:
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.sendall(data)
    conn.close()

except KeyboardInterrupt:
    exit()
