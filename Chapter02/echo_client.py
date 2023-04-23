# 간단한 에코 클라이언트 애플리케이션

import socket

import argparse

host = "localhost"


def echo_client(port):
    """a simple echo client"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the servr
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # Send data
    try:
        # Send data
        message = "Test message. This message will be echoed."
        print(f"Sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"Received: {len (data)} bytes [{data.decode ()}]")
    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"other exception: {str(e)}")
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
