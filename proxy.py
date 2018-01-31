import socket, sys
from _thread import *

MAX_CONN = 5
BUFFER_SIZE = 8192

def main():
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        print('Invalid number of arguments')
        return 0
    print('Port number', port)

    try:
        connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_socket.bind(('', port))
        connection_socket.listen(MAX_CONN)
        print('*** Server started at port', port)
    except Exception:
        print('Unable to start server: socket initialization failed')
        return -1

    # Main loop of proxy server
    while True:
        try:
            conn, addr = connection_socket.accept()
            data = conn.recv(BUFFER_SIZE)
            start_new_thread(create_connection, (conn, addr, data))
        except KeyboardInterrupt:
            connection_socket.close()
            print('\nConnection closed on port', port)
            return 0

def create_connection(conn, addr, data):
    print("Created a connection")
    try:
        url = data.split('\n')[0].split(' ')[1]
        http_pos = url.find('://')

        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]

        print(temp)
    except Exception:
        pass

main()
