# ------------------------------------------------------    
# --------------------- Control BDD --------------------
# ------------------------------------------------------  

import datetime

import pymysql.cursors

class BDD:
    """BDD object
    permit to connect to the BDD
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
        """configure the BDD

        Args:
            _host (str): host of the BDD
            _user (str): name of the user
            _password (str): password to connect the user
            _database (str): name of the database
        """
        self.hostG = _host
        self.userG = _user
        self.passwordG = _password
        self.databaseG = _database
    
# --------------------- Compo -------------------------

    def connectionBDD(self):
        """connection to the BDD

        Returns:
            pymysql: connection
        """
        connection= pymysql.connect(
            host= self.hostG,
            user= self.userG,
            password= self.passwordG,
            database= self.databaseG,
        )
        return connection

    def closeBDD(self, connection):
        """close the connection

        Args:
            connection (pymysql): connection

        Returns:
            pymysql: return the connection null
        """
        connection.commit()
        connection.close()
        return connection
        
# --------------------- GET -------------------------

    def getBDD(self):
        """get information of the BDD
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
        """insert data inside BDD
        """
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (datetime.datetime.today(), sortieA[0], sortieA[1], sortieA[2]))
        connection = self.closeBDD(connection)
    
# --------------------- DELETE ----------------------

    def deleteValue(self):
        """delete some values of the BDD
        """
        connection = self.connectionBDD()
        with connection.cursor() as cursor:
            sql= "DELETE FROM capteur"
            cursor.execute(sql)
            reponse = cursor.fetchall()
        connection = self.closeBDD(connection)
