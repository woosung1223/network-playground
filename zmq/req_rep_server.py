import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    message = socket.recv()
    print("received: ", str(message))

    time.sleep(1)

    socket.send(b"Hi!")