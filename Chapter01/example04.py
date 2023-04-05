# Byte Order

import socket


def convert_integer():
    data = 1234
    # 32 bit
    print(
        f"Original: {data} => "
        f"Long host byte order: {socket.ntohl(data)}, "
        f"Network byte order: {socket.htonl(data)}"
    )
    # 16 bit
    print(
        f"Original: {data} => "
        f"Short host byte order: {socket.ntohs(data)}, "
        f"Network byte order: {socket.htons(data)}"
    )


if __name__ == "__main__":
    convert_integer()
