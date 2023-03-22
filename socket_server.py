import socket

#port above 1024 because less than that it's reserved for standard internet protocol
def server_pro():
    #obtain host address
    host =socket.gethostname()
    port = 5000

    #get instance
    server_socket = socket.socket()
    #get host and port together
    server_socket.bind((host, port))

    server_socket.listen(2)
    #accept new connection
    conn, address = server_socket.accept()
    print("Connection from: "+ str(address))
    #we are using while to run the server and to wait for client request/messages
    while True:
        #receive data stream < 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        #send data to client
        conn.send(data.encode())

    #closing the connection
    conn.close()

if __name__ == '__main__':
    server_pro()