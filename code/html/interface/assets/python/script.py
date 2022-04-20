import sys
import socket

sys.path.append("/var/www/html/interface/python")
print(sys.path)
# --------------------- SCRIPT -------------------------

from Client import Client

client = Client()
client.configClient('192.168.0.10', 6780)
client.execute("GETRT")