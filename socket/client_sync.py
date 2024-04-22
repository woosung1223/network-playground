import socket

HOST = '127.0.0.1'
PORT = 12345

print('> echo-client is activated')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((HOST, PORT))

    while True:
        messageToSend = input('> ')
        clientSocket.sendall(bytes(messageToSend, 'utf-8'))
        receivedMessage = clientSocket.recv(1024)
        print('> received:', receivedMessage.decode('utf-8'))

        if messageToSend == 'quit':
            break

print('> echo-client is de-activated')