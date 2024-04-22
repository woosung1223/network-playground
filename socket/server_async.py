import socketserver
import threading

group_queue = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('> client connected by IP address {0} with Port number {1}'
              .format(self.client_address[0], self.client_address[1]))

        global group_queue
        group_queue.append(self.request)

        while True:
            receivedMessage = self.request.recv(1024)
            if receivedMessage.decode('utf-8') == 'quit':
                group_queue.remove(self.request)
                break

            print('> echoed: {0} by {1}'
                  .format(receivedMessage.decode('utf-8'), threading.current_thread()))
            for connection in group_queue:
                connection.sendall(receivedMessage)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        baseThreadNumber = threading.active_count()
        while True:
            msg = input('> ')
            if msg == 'quit':
                if baseThreadNumber == threading.active_count():
                    print('> stop')
                    break
                else:
                    print('> active thread: ', threading.active_count() - baseThreadNumber)

        print('> server shutdown')
        server.shutdown()
    
