import os
import socket
import threading
import socketserver

SERVER_HOST = "localhost"
SERVER_PORT = 0  # tells the kernel to pickup a port dynamically
BUF_SIZE = 1024
ECHO_MSG = "Hello echo server!"


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""

    pass


class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send the echo back to the client
        data = str(self.request.recv(BUF_SIZE), "UTF-8")

        current_process_id = os.getpid()
        response = f"{current_process_id}: [{data}]"
        print(f"Server sending response [current_process_id: data] = [{response}]")
        self.request.send(bytes(response, "UTF-8"))
        return


class ForkedClient:
    """A Client to test forking server"""

    def __init__(self, ip, port):
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        self.sock.connect((ip, port))

    def run(self):
        """Client playing with the server"""
        # Send the data to server
        current_process_id = os.getpid()
        print(
            f"PID {current_process_id} Sending echo message to the server : [{ECHO_MSG}]"
        )
        sent_data_length = self.sock.send(bytes(ECHO_MSG, "UTF-8"))
        print(f"Sent: {sent_data_length} characters, so far...")

        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print(f"PID {current_process_id} received: {response[5:]}")

    def shutdown(self):
        """Cleanup the client socket"""
        self.sock.close()


def main():
    # Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address  # Retrieve the port number
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.Daemon = True  # don't hang on exit
    server_thread.start()
    print(f"Server loop running PID: {os.getpid()}")

    # Launch the client(s)
    client1 = ForkedClient(ip, port)
    client1.run()
    print("First client running")

    client2 = ForkedClient(ip, port)
    client2.run()
    print("Second client running")

    # Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()


if __name__ == "__main__":
    main()
