# ------------------------------------------------------    
# --------------------- ControlerServer ----------------
# ------------------------------------------------------  

from FileControler import FileControler
from Actioner import Actioner

class Controler:
    """Controler object
        Determine what actions to take
    """

    def __init__(self, client_, adressClient_):
        """Constructor

        Args:
            client_ (str): IP of client
            adressClient_ (str): Port of client
        """
        self.client = client_
        self.adressClient = adressClient_


# ----------------- Config General ---------------------

    def initConfig(self):
        """general configuration
        """
        Actioner.sensor.configSensor(_average = 100.0)
        #self.servo.configServo(newCalibParam = {"port": 17, "mini_angle": 0, "maxi_angle": 180, "minPWM": 0.4/1000, "maxPWM": 2.4/1000})


# --------------------- Listen -------------------------

    def listening(self):
        """listen command sent by client

        Returns:
            str: command
        """
        command = self.client.recv(1024).decode()
        return command
    
    
# --------------------- Send ---------------------------

    def sending(self, message):
        """send command to client

        Args:
            message (str): message send to client

        Returns:
            str: Error
        """
        self.client.send(message)
        n = self.client.send(message)
        if (n != len(message)):
            return 'ERROR'
        

# --------------------- GETRT -----------------------

    def getRTcontroler(self,continu):
        """controler to get data in Real Time

        Args:
            continu (bool): permit to stop the RT

        Returns:
            str: End
        """
        while continu == True:
            print(continu)
            message = bytearray(str(Actioner.sensor.measures()), 'utf-8')
            self.sending(message)
            command = self.client.recv(1024).decode()
            continu = self.controlerCommand(command)
            print(command)
        return "end"
    
    
# --------------------- Calibrate -----------------------
    
    def calibrate(self, command):
        """Controler to calibrate the sensor

        Args:
            command (str): type and step for the calibration

        Returns:
            str: calibration progress
        """
        if (command[0]== 0):
            isCalibrate = Actioner.sensor.calibratePH(command[1])
        elif (command[0]== 1):
            isCalibrate = Actioner.sensor.calibrateOxygen(command[1])
        elif (command[0]== 2):
            isCalibrate = Actioner.sensor.calibrateConductivity(command[1])
        return isCalibrate
    
    
# --------------------- Servo -----------------------

    def servoControler(self,command):
        """Controler to servomotor

        Args:
            command (str): type and angle for rotate servomotor

        Returns:
            str: End
        """
        if (command[0]== "direct"):
            print("direct")
            Actioner.servo.rotateDirect(command[1])
        if (command[0]== "slow"):
            print("slow")
            FileControler.writePartPartFile("servo", "status", "continu")
            Actioner.servo.rotateSlow(command[1])
        if (command[0]== "stop"):
            print("stop")
            FileControler.writePartPartFile("servo", "status", "stop")
        return "end"
    
    
# --------------------- Controler -----------------------
    
    def controlerCommand(self, command):
        """General controler

        Args:
            command (str): Full command

        Returns:
            str: progress
        """
        print("controler")
        
        #-------------GETRT------------
        if (command == "GETDATA" or command == "GETRT" or command == "continu"):
            message = self.getRTcontroler(True)
        elif (command == "stop"):
            message = self.getRTcontroler(False)
            
        #-------------CALIBRATE------------
        elif ("CALIBRATE" in command):
            command = [int(command.split()[1]), float(command.split()[2])]
            message = self.calibrate(command)
            
        #-------------SERVO------------
        elif ("SERVO" in command) :
            print(command)
            command = [command.split()[1], int(command.split()[2])]
            message = self.servoControler(command)
            
        #-------------ERROR------------
        else:
            message = str.encode("ERREUR")
        return message

