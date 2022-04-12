import socket
import pymysql.cursors
import time
import datetime

HOST= '192.168.0.10'
PORT= 6782
client=''

#--------------------------FONCTION GLOBALE CLIENT------------------------------------------

def convert(string):
    string = string[:-1]
    string = string[1:]
    tab = string.split(',')
    sortie = [0,0,0]
    for i in range(3):
        sortie[i] = float(tab[i])
    return sortie
    
#---------------------CLIENT -> SERVEUR------------------------ 
   
def connection() :
    global client
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print ('connexion vers' + HOST + ':' + str(PORT) + 'reussie.')
    
def envoyer(message):
    global client
    n=client.send(str.encode(message))
    print ('envoi de :' + message)
    if (n != len(message)):
        print ('erreur envoi')
    else :
        print ('envoi ok.')
  
def recevoir() :
    global client 
    donnees = client.recv(4096).decode()
    print( 'Reception...')
    print (donnees)
    print ('Deconnexion')
    donnees = convert(donnees)
    return donnees


#-----------------------BDD------------------------------------


def connectionBDD():
     connection= pymysql.connect(
        host= 'localhost',
        user= 'user',
        password= 'pi',
        database= 'Rob',
    )
     return connection

def closeBDD(connection):
    connection.commit()
    connection.close()
    return connection   
        
def inssertBDD(donnees):
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (datetime.datetime.today(), round(donnees[0],4), round(donnees[1],4), round(donnees[2],4)))
    connection = closeBDD(connection)
    
def getBDD():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "SELECT * FROM capteur"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    print(reponse)


#----------------------------------------------------
    
def execute(message):
    global client
    connection()
    envoyer(message)
    donnees= recevoir()
    if message == 'GETDATA' :
        inssertBDD(donnees)
    elif message == 'GETRT' :
        i=0
        while i<10 :
            donnees = recevoir()
            inssertBDD(donnees)
            i=i+1
            client.send(str.encode('continu'))
    client.close()
#-------------------appel fonction --------------
 

execute('GETRT')