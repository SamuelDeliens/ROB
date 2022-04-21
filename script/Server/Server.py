# ------------------------------------------------------    
# --------------------- Server send --------------------
# ------------------------------------------------------  

import socket
import time

from Sensor import Sensor

class Server:

    def __init__(self):
        self.adress = ''
        self.port = 6788
        self.server = ''
        self.client = ''
        self.adressClient = ''
        self.sensor = Sensor()

# --------------------- Config -------------------------

    def configServer(self, _adress, _port):
        self.adress = _adress
        self.port = _port

# --------------------- Server -------------------------

    def createServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.adress, self.port))

    def closeServer(self):
        self.server.close()
        return 'END CONNECTION'

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

# --------------------- Controler -----------------------
    
    def controlerCommand(self, command):
        if (command == "GETDATA" or command == "GETRT" or command == "continu"):
            action = True
        else:
            message = str.encode("ERREUR")
            #sending = sending(message)
            action = False
        return action
    
# --------------------- Request -------------------------

    def doRequest(self):
        command = self.listening()
        continu = self.controlerCommand(command)
        while continu == True:
            print(continu)
            message = bytearray(str(self.sensor.measures()), 'utf-8')
            self.sending(message)
            command = self.client.recv(1024).decode()
            continu = self.controlerCommand(command)
            print(command)
    
# --------------------- Client ---------------------------

    def connection(self):
        self.createServer()
        while True:
            self.server.listen(1)
            self.client, self.adressClient = self.server.accept()
            self.doRequest()
        self.client.close()
