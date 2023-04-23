# 서비스 이름 찾기

import socket


def find_service_name():
    protocol_name = "tcp"
    for port in [80, 25]:
        print(
            f"Port: {port} => "
            f"service name: "
            f"{socket.getservbyport(port, protocol_name)}"  # Translate an internet port number and protocol name to a service name
        )
        print(f"Port: 53 => service name: " f"{socket.getservbyport(53, 'udp')}")


if __name__ == "__main__":
    find_service_name()
