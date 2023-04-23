# 소켓의 블로킹/논블로킹 모드 변경

import socket


def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)  # Set blocking mode
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print(f"Trivial Server lauched on socket: {str(socket_address)}")
    while 1:
        s.listen(1)


if __name__ == "__main__":
    test_socket_modes()
