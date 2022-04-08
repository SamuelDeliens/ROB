import socket
import mesure

ADRESS = ''
PORT = 6781
server, client, adressClient

def configServer(ADRESS, PORT):
    ADRESS = ADRESS
    PORT = PORT

# ----------------------- GLOBAL --------------------------------

def connectServerClient():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADRESS, PORT))
    server.listen(1)
    client, adressClient = server.accept()

def closeConnect():
    client.close()
    server.close()
    return 'FIN CONNEXION'

def controlerCommand(command):
    if (command == "GETDATA"):
        message = bytearray(str(mesure()), 'utf-8')
    else if (command == "GETRT"):
        getRT()
        return 'END RT'
    else:
        message = str.encode("erreur de commande")
    return messages

# ----------------------- ETAPE --------------------------------

def listening():
    command = client.recv(4096).decode()
    message = controlerCommand(command)
    return message
    
def sending(message):
    client.send(message)
    n = client.send(message)
    if (n != len(message)):
        return 'ERREUR ENVOI'
    
# ------------------------ COMPLET -----------------------------

def doRequest():
    connectServerClient()
    command = listening()
    action = controlerCommand(command)
    if (action != 'ERREUR'):
        while (action == TRUE)
            command = listening()
            action = controlerCommand(command)
            message = bytearray(str(mesure()), 'utf-8')
            sending(message)
    else:
        print(action)
    closeConnect() 
    