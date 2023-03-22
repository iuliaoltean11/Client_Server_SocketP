import socket

def client_pro():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    #connect to server
    client_socket.connect((host, port))

    #take the input
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        #send message
        client_socket.send(message.encode())
        #receive response from server
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client_pro()