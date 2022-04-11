import socket
import mesure

ADRESS = ''
PORT = 6781
server = ''
client = ''
adressClient = ''

def configServer(ADRESS1, PORT2):
    global ADRESS, PORT
    ADRESS = ADRESS1
    PORT = PORT2

# ----------------------- GLOBAL --------------------------------

def connectServerClient():
    global server, client, adressClient
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADRESS, PORT))
    server.listen(1)
    client, adressClient = server.accept()

def closeConnect():
    global server, client
    client.close()
    server.close()
    return 'FIN CONNEXION'

# ----------------------- ETAPE --------------------------------

def listening():
    global client
    command = client.recv(4096).decode()
    return command
    
def sending(message):
    global client
    client.send(message)
    n = client.send(message)
    if (n != len(message)):
        return 'ERREUR ENVOI'
    
def controlerCommand(command):
    if (command == "GETDATA"):
        message = bytearray(str(mesure.mesure()), 'utf-8')
        sending(message)
        action = False
    elif (command == "GETRT"):
        action = True
    else:
        message = str.encode("ERREUR")
        #sending = sending(message)
        action = False
    return False
    
# ------------------------ COMPLET -----------------------------

def doRequest():
    global client
    connectServerClient()
    command = listening()
    action = controlerCommand(command)
    continu = True
    while continu:
        message = bytearray(str(mesure.mesure()), 'utf-8')
        sending(message)
        data = client.recv(1024)
        print(data)
        if not data:
            continu = False
    closeConnect()
    
doRequest()