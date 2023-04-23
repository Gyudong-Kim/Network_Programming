import socket

PORT = 80
DATA = "GET /smain.html HTTP/1.1\r\n\r\n"

DNS = input("Web server DNS: ")
HOST = socket.gethostbyname(DNS)  # DNS 처리
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("HOST IP = " + HOST)
print("-----------------")

client.send(DATA.encode())  # To convert string to bytes at 3.6
response = client.recv(4096)  # bufsize 4096 bytes
print(response)

client.close()
