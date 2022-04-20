#------------------------------------------------------
#----------------------- Client -----------------------
#------------------------------------------------------

import socket
import pymysql.cursors
import time
import datetime

class Client:
    
    def __init__(self):
        self.HOST= '192.168.0.10'
        self.PORT= 6788
        self.client=''

#------------------------ CONFIGURATION ------------------------

    def configClient(self, _HOST, _PORT):
        self.HOST= _HOST
        self.PORT= _PORT
        self.client=''
#----------------------- FONCTION GLOBALE -----------------------

    def convert(self, string):
        string = string[:-1]
        string = string[1:]
        tab = string.split(',')
        sortie = [0,0,0]
        for i in range(3):
            sortie[i] = float(tab[i])
        return sortie
        
#--------------------- CLIENT -> SERVEUR -----------------------
       
    def connection(self) :
        self.client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        
    def envoyer(self, message):
        n = self.client.send(str.encode(message))
        if (n != len(message)):
            print ('erreur envoi')
        else :
            print ('envoi ok.')
      
    def recevoir(self) :
        donnees = self.client.recv(1024).decode()
        donnees = self.convert(donnees)
        return donnees

    def deconnection(self) :
        self.client.close()

#----------------------- BDD -----------------------


    def connectionBDD(self):
         connection= pymysql.connect(
            host= 'localhost',
            user= 'user',
            password= 'pi',
            database= 'Rov',
        )
         return connection

    def closeBDD(self, connection):
        connection.commit()
        connection.close()
        return connection   
            
    def inssertBDD(self, donnees):
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (datetime.datetime.today(), round(donnees[0],4), round(donnees[1],4), round(donnees[2],4)))
        connection = self.closeBDD(connection)
        
    def getBDD(self):
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "SELECT * FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)


#----------------------- Execution -----------------------
    def getData(self):
        donnees = self.recevoir()
        self.inssertBDD(donnees)
        self.client.send(str.encode('stop'))
    
    def getRT(self):
        nb = 2
        i=0
        while i<nb :
            donnees = self.recevoir()
            time.sleep(0.5) #delay insertion pour Interface
            self.inssertBDD(donnees)
            i=i+1
            if(i<nb):
                self.client.send(str.encode('continu'))
        self.client.send(str.encode('stop'))
        
    def controler(self, message):
        if(message == "GETDATA"):
            self.getData()
        elif(message == "GETRT"):
            self.getRT()

    def execute(self, message):
        self.connection()
        self.envoyer(message)
        self.controler(message)
        self.client.close()
        print("end")
        
        
        
#-------------------appel fonction --------------
