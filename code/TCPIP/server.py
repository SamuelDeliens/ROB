import socket
import pymysql.cursors

def connectionBDD():
    connection= pymysql.connect(
        host= 'localhost',
        user= 'root',
        password= 'pi',
        database= 'Rob',
    )
    return connection

def closeBDD(connection):
    connection.commit()
    connection.close()
    return connection

def getLastRow():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "SELECT * FROM capteur ORDER BY id DESC LIMIT 0,1"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    return reponse

def sendMSG(client, message):
    client.send(message)
    print('Envoie')  
    n = client.send(message)
    if (n != len(message)):
        print('Mauvais envoi')
    else:
        print('Good !') 

def controlCommand(command):
    if (command == "GETDATA"):
        message = bytearray(str(getLastRow()), 'utf-8')
        sendMSG(client, message)
    else if (command == "GETLDATA"):
        message = bytearray(str(getLastRow()), 'utf-8')
        sendMSG(client, message)    

ADRESS = ''
PORT = 6781

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ADRESS, PORT))
server.listen(1)
client, adressClient = server.accept()
print(adressClient)
print('connexion de '+ adressClient[0])

command = client.recv(4096).decode()
controlCommand(command)
        
print('Fermeture connexion !')
client.close()
print('Arret du serveur')
server.close()