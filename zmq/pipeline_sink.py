import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5557")

result = 0
for i in range(0, 3):
    taskDone = socket.recv_pyobj()
    result += taskDone

print("result:", result)