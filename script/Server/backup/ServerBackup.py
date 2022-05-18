# ------------------------------------------------------    
# --------------------- Server send --------------------
# ------------------------------------------------------  

import socket
import time

from FileControler import FileControler
from Sensor import Sensor
from ServoMotor import ServoMotor

class Server:

    def __init__(self):
        self.calibServer = {"adress": '', "port": 6788}
        self.server = ''
        self.client = ''
        self.adressClient = ''
        self.sensor = Sensor()
        self.servo = ServoMotor()
        self.fileControler = FileControler()
        
        
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


# --------------------- GETRT -----------------------

    def getRTcontroler(self,command):
        while continu == True:
            print(continu)
            message = bytearray(str(self.sensor.measures()), 'utf-8')
            self.sending(message)
            command = self.client.recv(1024).decode()
            continu = self.controlerCommand(command)
            print(command)
        return "end"
    
    
# --------------------- Calibrate -----------------------
    
    def calibrate(self, command):
        if (command[0]== 0):
            isCalibrate = self.sensor.calibratePH(command[1])
        elif (command[0]== 1):
            isCalibrate = self.sensor.calibrateOxygen(command[1])
        elif (command[0]== 2):
            isCalibrate = self.sensor.calibrateConductivity(command[1])
        return isCalibrate
    
    
# --------------------- Servo -----------------------

    def servoControler(self,command):
        if (command[0]== "direct"):
            print("direct")
            self.servo.rotateDirect(command[1])
        if (command[0]== "slow"):
            print("slow")
            self.fileControler.writePartPartFile("servo", "status", "continu")
            self.servo.rotateSlow(command[1])
        if (command[0]== "stop"):
            print("stop")
            self.fileControler.writePartPartFile("servo", "status", "stop")
        return "end"
    
    
# --------------------- Controler -----------------------
    
    def controlerCommand(self, command):
        print("controler")
        
        #-------------GETRT------------
        if (command == "GETDATA" or command == "GETRT" or command == "continu"):
            message = getRTcontroler(True)
        elif (command == "stop"):
            message = getRTcontroler(False)
            
        #-------------CALIBRATE------------
        elif ("CALIBRATE" in command):
            command = [int(command.split()[1]), float(command.split()[2])]
            message = self.calibrate(command)
            
        #-------------SERVO------------
        elif ("SERVO" in command) :
            print(command)
            command = [command.split()[1], int(command.split()[2])]
            message = self.servoControler(command)
            
        #-------------ERROR------------
        else:
            message = str.encode("ERREUR")
        return message

    
# --------------------- Request -------------------------

    def doRequest(self):
        command = self.listening()
        message = self.controlerCommand(command)
        self.sending(str.encode(message))
    
# --------------------- Client ---------------------------

    def connection(self):
        self.createServer()
        while True:
            print("-----------------new----------------")
            self.server.listen(1)
            self.client, self.adressClient = self.server.accept()
            self.doRequest()
        self.client.close()

