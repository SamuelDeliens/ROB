# ------------------------------------------------------    
# --------------------- Control BDD --------------------
# ------------------------------------------------------  

import time
import datetime

import pymysql.cursors

class BDD:
    """BDD object
    manage the BDD table capteur
    """

    def __init__(self):
        """Constructor
        """
        self.hostG = 'localhost'
        self.userG = 'root'
        self.passwordG = 'pi'
        self.databaseG = 'Rov'

# --------------------- Config -------------------------

    def configBDD(self, _host, _user, _password, _database):
        """configuration of the BDD

        Args:
            _host (str): host of the user
            _user (str): name of the user
            _password (str): password to connect the user
            _database (str): name of the database choosen
        """
        self.hostG = _host
        self.userG = _user
        self.passwordG = _password
        self.databaseG = _database
    
# --------------------- Compo -------------------------

    def connectionBDD(self):
        """connection to the BDD

        Returns:
            str: connecion to BDD to make request
        """
        connection= pymysql.connect(
            host= self.hostG,
            user= self.userG,
            password= self.passwordG,
            database= self.databaseG,
        )
        return connection

    def closeBDD(self, connection):
        """close connection to BDD

        Args:
            connection (str): the connection already make

        Returns:
            str: connection end
        """
        connection.commit()
        connection.close()
        return connection
        
# --------------------- GET -------------------------

    def getBDD(self):
        """get every data from the BDD
        """
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "SELECT * FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)
        print(reponse)
    
# --------------------- ADD -------------------------

    def inssertBDD(self, sortieA):
        """insert data into BDD

        Args:
            sortieA (array): values of the sensors
        """
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (datetime.datetime.today(), sortieA[0], sortieA[1], sortieA[2]))
        connection = self.closeBDD(connection)
    
# --------------------- DELETE ----------------------

    def deleteValue(self):
        """delete data from the BDD
        """
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "DELETE FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)
