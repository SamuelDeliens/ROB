# ------------------------------------------------------    
# --------------------- Server send --------------------
# ------------------------------------------------------  

import socket
from ThreadClient import ThreadClient

class Server:
    """Server object
    manage the TCPIP server connection
    """

    def __init__(self):
        """Constructor
        """
        self.calibServer = {"adress": '', "port": 6780}
        self.listThreads = []


# --------------------- Config -------------------------

    def configServer(self, adress, port):
        """configuration of the server
        
        Args:
            adress (str): ip adress of the connection
            port (str): port adress of the connection
        """
        self.calibServer["adress"] = adress
        self.calibServer["port"] = port


# --------------------- Server -------------------------

    def createServer(self):
        """create the server connection
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.calibServer["adress"], self.calibServer["port"]))

    def closeServer(self):
        """close the connection
        
        Returns:
            str: END CONNECTION
        """
        self.server.close()
        return 'END CONNECTION'


# --------------------- Server ---------------------------

    def connection(self):
        """general function to manage the TCPIP server
        """
        self.createServer()
        while True:
            while True:
                print("-----------------new----------------")
                self.server.listen(1)
                self.client, self.adressClient = self.server.accept()
                threadClient = ThreadClient(self.client, self.adressClient)
                threadClient.start()
                self.listThreads.append(threadClient)
            
            for threadX in self.listThreads:
                threadX.join()
        self.client.close()
