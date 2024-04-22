import zmq
import time
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

areas = ["Suwon", "Yongin", "Seoul"]

while True:
    area = areas[randrange(0, len(areas))]

    message = "{0}".format(area)
    print(message)
    
    time.sleep(1)

    socket.send_string(message)