#------------------------------------------------------
#----------------------- Script -----------------------
#------------------------------------------------------

import sys
import socket

sys.path.append("/var/www/html/interface/python")
print(sys.path)

from Client import Client
from BDD import BDD

client = Client()

#----------------------- Config -----------------------

client.configClient('192.168.0.10', 6780)
client.BDD.configBDD('localhost', 'user', 'pi', 'Rov')

# --------------------- SCRIPT -------------------------

client.execute("GETRT")