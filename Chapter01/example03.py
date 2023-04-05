# 서비스 이름 찾기

import socket


def find_service_name():
    protocolname = "tcp"
    for port in [80, 25]:
        print(
            f"Port: {port} => "
            f"service name: "
            f"{socket.getservbyport(port, protocolname)}"
        )
        print(f"Port: 53 => service name: " f"{socket.getservbyport(53, 'udp')}")


if __name__ == "__main__":
    find_service_name()
