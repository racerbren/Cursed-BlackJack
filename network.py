import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()


    def getOtherPlayer(self):
        if int(self.player) == 0:
            return 1
        else:
            return 0


    def getPlayer(self):
        return self.player


    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096).decode()


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)