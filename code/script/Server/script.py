# ------------------------------------------------------    
# ---------------------- Script-------------------------
# ------------------------------------------------------

from Server import Server
from FileControler import FileControler
from Actioner import Actioner

adress = ''
port = 6780

server = Server()

# --------------------- SCRIPT -------------------------

server.configServer(adress, port)
server.connection()
