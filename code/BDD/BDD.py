# ------------------------------------------------------    
# --------------------- Control BDD --------------------
# ------------------------------------------------------  

import pymysql.cursors
import time
import datetime

hostG = 'localhost'
userG = 'root'
passwordG = 'pi'
databaseG = 'Rob'

# --------------------- Config -------------------------

def configBDD(_host, _user, _password, _database):
    global hostG, userG, passwordG, databaseG
    hostG = _host
    userG = _user
    passwordG = _password
    databaseG = _database
    
# --------------------- Compo -------------------------

def connectionBDD():
    global hostG, userG, passwordG, databaseG
    connection= pymysql.connect(
        host= hostG,
        user= userG,
        password= passwordG,
        database= databaseG,
    )
    return connection

def closeBDD(connection):
    connection.commit()
    connection.close()
    return connection
        
# --------------------- GET -------------------------

def getBDD():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "SELECT * FROM capteur"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    print(reponse)
    
# --------------------- ADD -------------------------

def inssertBDD(sortieA):
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (datetime.datetime.today(), sortieA[0], sortieA[1], sortieA[2]))
    connection = closeBDD(connection)
    
# --------------------- DELETE ----------------------

def deleteValue():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "DELETE FROM capteur"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)