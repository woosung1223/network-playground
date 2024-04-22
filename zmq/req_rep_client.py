import zmq

context = zmq.Context()

print("Connecting to the server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    socket.send(b"Hello")

    message = socket.recv()
    print("received reply: ", str(message))