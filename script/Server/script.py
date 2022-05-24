# ------------------------------------------------------    
# ---------------------- Script-------------------------
# ------------------------------------------------------

from Server import Server

adress = ''
port = 6780

server = Server()

# --------------------- SCRIPT -------------------------

server.configServer(adress, port)
server.connection()