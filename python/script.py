#------------------------------------------------------
#----------------------- Script -----------------------
#------------------------------------------------------

import sys
import socket

sys.path.append("/var/www/html/interface/python")
print(sys.path)

from Client import Client
from BDD import BDD
from FileControler import FileControler


type_ = sys.argv[1]
action_ = sys.argv[2]

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
            fileControler.writeFile("continu")
            client.execute("GETRT")
        elif(action_ == "stop"):
            fileControler.writeFile("stop")

# --------------------- SCRIPT -------------------------

config()
controler()