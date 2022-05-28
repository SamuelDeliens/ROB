# ------------------------------------------------------    
# --------------------- Control BDD --------------------
# ------------------------------------------------------  

import time
import datetime

import pymysql.cursors

class BDD:

    def __init__(self):
        self.hostG = 'localhost'
        self.userG = 'root'
        self.passwordG = 'pi'
        self.databaseG = 'Rov'

# --------------------- Config -------------------------

    def configBDD(self, _host, _user, _password, _database):
        self.hostG = _host
        self.userG = _user
        self.passwordG = _password
        self.databaseG = _database
    
# --------------------- Compo -------------------------

    def connectionBDD(self):
        connection= pymysql.connect(
            host= self.hostG,
            user= self.userG,
            password= self.passwordG,
            database= self.databaseG,
        )
        return connection

    def closeBDD(self, connection):
        connection.commit()
        connection.close()
        return connection
        
# --------------------- GET -------------------------

    def getBDD(self):
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "SELECT * FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)
        print(reponse)
    
# --------------------- ADD -------------------------

    def inssertBDD(self, sortieA):
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (datetime.datetime.today(), sortieA[0], sortieA[1], sortieA[2]))
        connection = self.closeBDD(connection)
    
# --------------------- DELETE ----------------------

    def deleteValue(self):
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "DELETE FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)
