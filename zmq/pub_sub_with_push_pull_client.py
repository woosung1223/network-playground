import zmq
import random
import time

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "") # receive all messages

publisher = context.socket(zmq.PUSH)
publisher.connect("tcp://localhost:5557")

while True:
    message = random.randrange(0, 100)
    print("sended:", message)
    publisher.send_string(str(message))
    
    time.sleep(2)

    received = subscriber.recv_string()
    print("received: ", received)
