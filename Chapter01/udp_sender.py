import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "KNUE Technology"

print("UDP target IP: ", UDP_IP)
print("UDP target PORT: ", UDP_PORT)
print("message: ", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = MESSAGE.encode()

for i in range(2):
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(1)
