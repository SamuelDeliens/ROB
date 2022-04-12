# ------------------------------------------------------    
# --------------------- Server send --------------------
# ------------------------------------------------------  

import socket
import measure

adress = ''
port = 6781
server = ''
client = ''
adressClient = ''

# --------------------- Config -------------------------

def configServer(_adress, _port):
    global adress, port
    adress = _adress
    port = _port

# --------------------- Compo -------------------------

def connectServerClient():
    global adress, port, server, client, adressClient
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((adress, port))
    server.listen(1)
    client, adressClient = server.accept()

def closeConnect():
    global server, client
    client.close()
    server.close()
    return 'END CONNECTION'

# --------------------- Listen -------------------------

def listening():
    global client
    command = client.recv(4096).decode()
    return command
    
# --------------------- Send ---------------------------

def sending(message):
    global client
    client.send(message)
    n = client.send(message)
    if (n != len(message)):
        return 'SEND ERROR'
    
# --------------------- Controler -----------------------
    
def controlerCommand(command):
    if (command == "GETDATA"):
        message = bytearray(str(mesure.measure()), 'utf-8')
        sending(message)
        action = False
    elif (command == "GETRT"):
        action = True
    else:
        message = str.encode("ERREUR")
        #sending = sending(message)
        action = False
    return False
    
# --------------------- Request -------------------------

def doRequest():
    global client
    connectServerClient()
    command = listening()
    action = controlerCommand(command)
    continu = True
    #while continu
    while True:
        message = bytearray(str(measure.measure()), 'utf-8')
        sending(message)
        data = client.recv(1024)
        print(data)
        if not data:
            break
            #continu = False
    closeConnect()
    
doRequest()