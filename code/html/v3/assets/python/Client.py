#------------------------------------------------------
#----------------------- Client -----------------------
#------------------------------------------------------

import socket
import time
import datetime

import pymysql.cursors

from BDD import BDD
from FileControler import FileControler

class Client:
    """Client object
    manage the TCPIP client connection
    """
    def __init__(self):
        """Constructor
        """
        self.HOST= '192.168.0.10'
        self.PORT= 6780
        self.client=''
        self.status = {"GETRT": {"status": "stop"}}
        self.BDD= BDD()
        self.fileControler = FileControler()


#------------------------ Config ------------------------

    def configClient(self, _HOST, _PORT):
        """configuration of the client

        Args:
            _HOST (str): ip adress of the connection
            _PORT (str): port adress of the connection
        """
        self.HOST= _HOST
        self.PORT= _PORT
        self.client=''
        self.status = self.fileControler.readFile()
        
        
#----------------------- String -> Tab ------------------

    def convert(self, string):
        """decomposed the command to an array

        Args:
            string (str): command string

        Returns:
            array: command decomposed
        """
        print(string)
        string = string[:-1]
        string = string[1:]
        tab = string.split(',')
        sortie = [0,0,0]
        for i in range(3):
            sortie[i] = float(tab[i])
        return sortie
        
        
#--------------------- Client -> Server -------------------
       
    def connection(self) :
        """connection to the Server
        """
        self.client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        print("connected")
        
    def sendMsg(self, message):
        """send any message to the Server

        Args:
            message (str): message send
        """
        n = self.client.send(str.encode(message))
        if (n != len(message)):
            print ('erreur envoi')
        else :
            print ('envoi ok.')
      
    def receive(self) :
        """receave message from server

        Returns:
            str: message receave
        """
        donnees = self.client.recv(1024).decode()
        donnees = self.convert(donnees)
        return donnees

    def deconnection(self) :
        """deconnection with the Server
        """
        self.client.close()
        

#----------------------- Execution DATA -----------------------
        
    def getData(self):
        """general function to get one data
        """
        donnees = self.receive()
        self.BDD.inssertBDD(donnees)
        self.sendMsg('stop')
        isFinish = self.client.recv(1024).decode()
        print(isFinish)
    
    def getRT(self):
        """general function to get data in RT
        """
        self.status = self.fileControler.readFile()
        while self.status["GETRT"]["status"] == "continu" :
            donnees = self.receive()
            donnees = self.receive()
            time.sleep(0.5) #delay insertion pour Interface
            self.BDD.inssertBDD(donnees)
            self.status = self.fileControler.readFile()
            if(self.status["GETRT"]["status"] == "continu"):
                self.sendMsg('continu')
        self.sendMsg('stop')
        isFinish = self.client.recv(1024).decode()
        print(isFinish)
        
    def calibrate(self):
        """general function to calibrate the sensor
        """
        isCalibrate = self.client.recv(1024).decode()
        print(isCalibrate)
        
#----------------------- Execution Sensor-----------------------
    
    def servo(self):
        """general function to control the servo
        """
        isMove = self.client.recv(1024).decode()
        print(isMove)
    
#----------------------- Controler -----------------------
        
    def controler(self, message):
        """Controler to manage the Client

        Args:
            message (str): command
        """
        if(message == "GETDATA"):
            self.getData()
        elif(message == "GETRT"):
            self.getRT()
        elif("CALIBRATE" in message):
            self.calibrate()
        elif("SERVO" in message):
            self.servo() 

    def execute(self, message):
        """general function for connection with the Server

        Args:
            message (str): command
        """
        self.connection()
        self.sendMsg(message)
        self.controler(message)
        self.deconnection()
        print("end")
