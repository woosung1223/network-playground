import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.DEALER)

clientNumber = sys.argv[1]
identity = u'%s' % clientNumber

socket.identity = identity.encode("ascii")
socket.connect("tcp://localhost:5570")

poll = zmq.Poller()
poll.register(socket, zmq.POLLIN)

while True:
    socket.send_string("request by #{0}".format(clientNumber))
    time.sleep(1)

    sockets = dict(poll.poll(1000))
    if socket in sockets:
        message = socket.recv()
        print("{0} received: {1}".format(identity, message))