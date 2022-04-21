# ------------------------------------------------------    
# ---------------------- Script-------------------------
# ------------------------------------------------------

from Sensor import Sensor
from Server import Server

offset = 0.40
average = 100.0

adress = ''
port = 6780

server = Server()

# --------------------- Config -------------------------

server.configServer(adress, port)
server.sensor.configSensor(offset, average)

# --------------------- SCRIPT -------------------------

server.connection()