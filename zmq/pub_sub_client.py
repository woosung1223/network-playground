import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")

area = sys.argv[1]
socket.setsockopt_string(zmq.SUBSCRIBE, area)

print("this area is", area)

while True:
    message = socket.recv_string()
    print("area {0} has recieved message"
          .format(area))
    