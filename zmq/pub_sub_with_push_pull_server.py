import zmq

context = zmq.Context()

publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5556")

subscriber = context.socket(zmq.PULL)
subscriber.bind("tcp://*:5557")

while True:
    message = subscriber.recv_string()
    publisher.send_string(message)
