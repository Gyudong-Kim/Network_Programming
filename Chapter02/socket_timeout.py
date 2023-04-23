# Socket timeout

import socket


def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Default socket time: {s.gettimeout()}")
    s.settimeout(100)
    print(f"Current socket timeout: {s.gettimeout()}")


if __name__ == "__main__":
    test_socket_timeout()
