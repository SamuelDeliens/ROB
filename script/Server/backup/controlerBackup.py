# ------------------------------------------------------    
# --------------------- ControlerServer ----------------
# ------------------------------------------------------  

import socket
import time

from FileControler import FileControler
from Actioner import Actioner
from Sensor import Sensor
from ServoMotor import ServoMotor

class Controler:

    def __init__(self, client_, adressClient_):
        self.client = client_
        self.adressClient = adressClient_


# ----------------- Config General ---------------------

    def initConfig(self):
        self.sensor.configSensor(_average = 100.0)
        #self.servo.configServo(newCalibParam = {"port": 17, "mini_angle": 0, "maxi_angle": 180, "minPWM": 0.4/1000, "maxPWM": 2.4/1000})


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
            FileControler.writePartPartFile("servo", "status", "continu")
            self.servo.rotateSlow(command[1])
        if (command[0]== "stop"):
            print("stop")
            FileControler.writePartPartFile("servo", "status", "stop")
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


