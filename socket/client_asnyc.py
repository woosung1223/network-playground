import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receiveHandler(clientSocket):
    while True:
        receivedData = clientSocket.recv(1024)
        print ('> received:', receivedData.decode('utf-8'))

        if receivedData.decode('utf-8') == 'quit':
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        
        try:
            if clientSocket.connect((HOST, PORT)) == -1:
                clientSocket.close()
                return
            
        except Exception as exceptionObj:
            print(Exception)
            return
        
        clientThread = threading.Thread(target=receiveHandler, args=(clientSocket,))
        clientThread.daemon = True
        clientThread.start()

        while True:
            sendMessage = input('> ')
            clientSocket.sendall(bytes(sendMessage, 'utf-8'))
            if sendMessage == 'quit':
                break

if __name__ == '__main__':
    main()