import zmq
import threading

class ServerTask(threading.Thread):

    def __init__(self, serverCount):
        threading.Thread.__init__(self)
        self.serverCount = serverCount

    def run(self):
        context = zmq.Context()

        frontend = context.socket(zmq.ROUTER)
        frontend.bind("tcp://*:5556")

        backend = context.socket(zmq.DEALER)
        backend.bind("inproc://backend")

        