import zmq

context = zmq.Context()

# connect Ventilator
subscriber = context.socket(zmq.PULL)
subscriber.connect("tcp://localhost:5556")

task = subscriber.recv_pyobj()
result = 0
for each in task:
    result += each

# connect Sink
publisher = context.socket(zmq.PUSH)
publisher.connect("tcp://localhost:5557")

publisher.send_pyobj(result)