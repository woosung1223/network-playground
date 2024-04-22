import zmq
import time

tasks = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

context = zmq.Context()
publisher = context.socket(zmq.PUSH)
publisher.bind("tcp://*:5556")

# prevent 'slow joiner' syndrome
time.sleep(10)

for task in tasks:
    publisher.send_pyobj(task)