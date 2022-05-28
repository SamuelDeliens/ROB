#------------------------------------------------------
#----------------------- Thread -----------------------
#------------------------------------------------------

from threading import Thread
from socketserver import ThreadingMixIn

from Controler import Controler

class ThreadClient(Thread):
    """Thread of one client
    manage the connection with one client
    
    Args:
        Thread (Thread): Thread of client
    """
    
    def __init__(self, client_, adressClient_):
        """Constructor
        
        Args:
            client_ (str): IP of connection
            adressClient_ (str): port of connection
        """
        Thread.__init__(self)
        self.client = client_
        self.adressClient = adressClient_
        self.controler = Controler(self.client, self.adressClient)
        

# --------------------- Listen -------------------------

    def listening(self):
        """listen for command
        
        Returns:
            str: command receave
        """
        command = self.client.recv(1024).decode()
        return command
    
    
# --------------------- Send ---------------------------

    def sending(self, message):
        """send message
        
        Args:
            message (str): message to send
            
        Returns:
            str: Error
        """
        self.client.send(message)
        n = self.client.send(message)
        if (n != len(message)):
            return 'ERROR'


# --------------------- Request -------------------------

    def run(self):
        """script of the connection with one client
        """
        self.controler.initConfig()
        command = self.listening()
        message = self.controler.controlerCommand(command)
        self.sending(str.encode(message))