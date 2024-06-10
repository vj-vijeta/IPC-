import socket
import os

SERVER_ADDRESS = '/tmp/ipc_socket'

def start_server():
    # Ensure the socket does not already exist
    try:
        os.unlink(SERVER_ADDRESS)
    except FileNotFoundError:
        pass
    except OSError:
        if os.path.exists(SERVER_ADDRESS):
            raise

    # Create a Unix Domain Socket
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        try:
            # Bind the socket to the address
            sock.bind(SERVER_ADDRESS)
            # Listen for incoming connections
            sock.listen(1)
            print(f'Server listening on {SERVER_ADDRESS}')

            while True:
                # Wait for a connection
                connection, client_address = sock.accept()
                with connection:
                    print('Client connected')
                    while True:
                        data = connection.recv(1024)
                        if data:
                            print('Received:', data.decode())
                            connection.sendall(data)  # Echo the data back to the client
                        else:
                            break
        except Exception as e:
            print(f'Error: {e}')
        finally:
            if os.path.exists(SERVER_ADDRESS):
                os.unlink(SERVER_ADDRESS)

if __name__ == '__main__':
    start_server()
