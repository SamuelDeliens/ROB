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
    
    def __init__(self):
        self.HOST= '192.168.0.10'
        self.PORT= 6780
        self.client=''
        self.BDD= BDD()
        self.fileControler = FileControler()


#------------------------ Config ------------------------

    def configClient(self, _HOST, _PORT):
        self.HOST= _HOST
        self.PORT= _PORT
        self.client=''
        
        
#----------------------- String -> Tab ------------------

    def convert(self, string):
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
        self.client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        
    def sendMsg(self, message):
        n = self.client.send(str.encode(message))
        if (n != len(message)):
            print ('erreur envoi')
        else :
            print ('envoi ok.')
      
    def receive(self) :
        donnees = self.client.recv(1024).decode()
        donnees = self.convert(donnees)
        return donnees

    def deconnection(self) :
        self.client.close()
        

#----------------------- Execution -----------------------
        
    def getData(self):
        donnees = self.receive()
        self.BDD.inssertBDD(donnees)
        self.sendMsg('stop')
    
    def getRT(self):
        status = self.fileControler.readFile()
        while status == "continu" :
            donnees = self.receive()
            donnees = self.receive()
            time.sleep(0.5) #delay insertion pour Interface
            self.BDD.inssertBDD(donnees)
            status = self.fileControler.readFile()
            if(status == "continu"):
                self.sendMsg('continu')
        self.sendMsg('stop')
        
    def controler(self, message):
        if(message == "GETDATA"):
            self.getData()
        elif(message == "GETRT"):
            self.getRT()

    def execute(self, message):
        self.connection()
        self.sendMsg(message)
        self.controler(message)
        self.deconnection()
        print("end")
        
        
        
#-------------------appel fonction --------------
