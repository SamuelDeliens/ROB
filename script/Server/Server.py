# ------------------------------------------------------    
# --------------------- Server send --------------------
# ------------------------------------------------------  

import socket
from ThreadClient import ThreadClient

class Server:

    def __init__(self):
        self.calibServer = {"adress": '', "port": 6780}
        self.listThreads = []


# --------------------- Config -------------------------

    def configServer(self, adress, port):
        self.calibServer["adress"] = adress
        self.calibServer["port"] = port


# --------------------- Server -------------------------

    def createServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.calibServer["adress"], self.calibServer["port"]))

    def closeServer(self):
        self.server.close()
        return 'END CONNECTION'


# --------------------- Server ---------------------------

    def connection(self):
        self.createServer()
        while True:
            while True:
                print("-----------------new----------------")
                self.server.listen(1)
                self.client, self.adressClient = self.server.accept()
                threadClient = ThreadClient(self.client, self.adressClient)
                threadClient.start()
                self.listThreads.append(threadClient)
            
            for threadX in self.listThreads:
                threadX.join()
        self.client.close()
