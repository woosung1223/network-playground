import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_string()
    print("received: ", message)

    messageToSend = input("> ")
    socket.send_string(messageToSend)