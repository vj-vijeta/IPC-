import socket
import os

SERVER_ADDRESS = '/tmp/ipc_socket'

def start_server():
    # Make sure the socket does not already exist
    try:
        os.unlink(SERVER_ADDRESS)
    except OSError:
        if os.path.exists(SERVER_ADDRESS):
            raise

    # Create a UDS (Unix Domain Socket)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        # Bind the socket to the address
        sock.bind(SERVER_ADDRESS)

        # Listen for incoming connections
        sock.listen(1)
        print(f'Server listening on {SERVER_ADDRESS}')

        while True:
            # Wait for a connection
            connection, client_address = sock.accept()
            try:
                print('Client connected:', client_address)
                
                while True:
                    data = connection.recv(1024)
                    if data:
                        print('Received:', data.decode())
                        connection.sendall(data)  # Echo the data back to the client
                    else:
                        break
            finally:
                connection.close()

if __name__ == '__main__':
    start_server()
