# ------------------------------------------------------    
# ---------------------- Script-------------------------
# ------------------------------------------------------

from Sensor import Sensor
from Server import Server

average = 100.0

adress = ''
port = 6780

server = Server()

# --------------------- Config -------------------------

server.configServer(adress, port)
server.sensor.configSensor(average)

# --------------------- SCRIPT -------------------------

server.connection()