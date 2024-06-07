import socket
import sys

SERVER_ADDRESS = '/tmp/ipc_socket'

def send_message(message):
    # Create a UDS (Unix Domain Socket)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        # Connect the socket to the server address
        sock.connect(SERVER_ADDRESS)

        try:
            # Send data
            print(f'Sending: {message}')
            sock.sendall(message.encode())

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += len(data)
                print(f'Received: {data.decode()}')

        finally:
            sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <message>')
        sys.exit(1)

    message = sys.argv[1]
    send_message(message)
