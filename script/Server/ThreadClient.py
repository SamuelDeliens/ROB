import socket
from threading import Thread
from socketserver import ThreadingMixIn

from Controler import Controler

class ThreadClient(Thread):
    def __init__(self, client_, adressClient_):
        Thread.__init__(self)
        self.client = client_
        self.adressClient = adressClient_
        self.controler = Controler(self.client, self.adressClient)
        

# --------------------- Listen -------------------------

    def listening(self):
        command = self.client.recv(1024).decode()
        return command
    
    
# --------------------- Send ---------------------------

    def sending(self, message):
        self.client.send(message)
        n = self.client.send(message)
        if (n != len(message)):
            return 'ERROR'


# --------------------- Request -------------------------

    def run(self):
        self.controler.initConfig()
        command = self.listening()
        message = self.controler.controlerCommand(command)
        self.sending(str.encode(message))