import measure
import BDD
import server

    # ============================================================
    # Script
    # ============================================================

offset = 0.40
moyenne = 100.0
adc = MCP3008()
accuracy = 3

host = 'localhost'
user = 'root'
password = 'pi'
database = 'Rob'

adress = ''
port = 6781

# --------------------- Config -------------------------

configMesure(offset, moyenne, adc)
configBDD(host, user, password, database)
configServer(adress, port)

# --------------------- SCRIPT -------------------------