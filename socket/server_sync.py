import socket

HOST = '127.0.0.1'
PORT = 12345

print('> echo server is started')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()

    clientSocket, clientAddress = serverSocket.accept()
    
    with clientSocket:
        print('> client connected by IP address {0} with port number {1}'
              .format(clientAddress[0], clientAddress[1]))
        
        while True:
            receivedMessage = clientSocket.recv(1024)
            print('> echoed:' , receivedMessage.decode('utf-8'))
            clientSocket.sendall(receivedMessage)

            if receivedMessage.decode('utf-8') == 'quit':
                break
    
    print ('> echo server is de-activated')