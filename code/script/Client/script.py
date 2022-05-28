#------------------------------------------------------
#----------------------- Script -----------------------
#------------------------------------------------------

import sys
import socket

sys.path.append("/var/www/html/assets/python")
print(sys.path)

from Client import Client
from BDD import BDD
from FileControler import FileControler

if len(sys.argv) > 1:
    type_ = sys.argv[1]
if len(sys.argv) > 2:
    action_ = sys.argv[2]
if len(sys.argv) > 3:
    step_ = sys.argv[3]

client = Client()
fileControler = FileControler()

#----------------------- Function Global ---------------------

def config():
    client.configClient('192.168.0.10', 6780)
    client.BDD.configBDD('localhost', 'user', 'pi', 'Rov')
    
def controler():
    if(type_ == "GETDATA"):
        client.execute("GETDATA")
    elif(type_ == "GETRT"):
        if(action_ == "launch"):
            fileControler.writeStatus("GETRT", "continu")
            client.execute("GETRT")
        elif(action_ == "stop"):
            fileControler.writeStatus("GETRT", "stop")
    elif(type_ == "CALIBRATE"):
        client.execute("CALIBRATE "+ action_ +" "+ step_)
    elif(type_ == "SERVO"):
        client.execute("SERVO "+ action_ +" "+ step_)
    elif(type_ == "CAMERA"):
        print("here")
        client.execute("CAMERA "+ action_)

# --------------------- SCRIPT -------------------------

config()
controler()