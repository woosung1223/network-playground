import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
print("Connecting to the server...")
socket.connect("tcp://localhost:5555")

while True:
    message = input("> ")
    socket.send_string(message)

    message = socket.recv_string()
    print("received reply: ", message)