# IPv4 주소 변환

import socket
from binascii import hexlify


def convert_ip4_address():
    for ip_addr in ["127.0.0.1", "192.168.0.1"]:
        packed_ip_addr = socket.inet_aton(
            ip_addr
        )  # Convert an IPv4 address from dotted-quad string format
        unpacked_ip_addr = socket.inet_ntoa(
            packed_ip_addr
        )  # Convert a 32bit packed IPv4 address to its standard dotted-quad string representation
        print(
            f"IP address: {ip_addr} => "
            f"Packed: {hexlify(packed_ip_addr)}, "  # Convert between binary and various ASCII-encoded binary representations
            f"Unpacked: {unpacked_ip_addr}"
        )


if __name__ == "__main__":
    convert_ip4_address()
