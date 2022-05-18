# ------------------------------------------------------    
# --------------------- Servo Motor -----------------
# ------------------------------------------------------

from time import sleep
from gpiozero import AngularServo

from FileControler import FileControler


class ServoMotor :
    
    def __init__(self):
        self.fileControler = FileControler()
        self.calibParam = {"port": 17, "mini_angle": 0, "maxi_angle": 180, "minPWM": 0.4/1000, "maxPWM": 2.4/1000}
        self.angle = float(self.fileControler.readFile()["servo"]["angle"])
        self.speed = float(self.fileControler.readFile()["servo"]["speed"])
        self.servo = AngularServo(self.calibParam["port"], min_angle=self.calibParam["mini_angle"], max_angle=self.calibParam["maxi_angle"], min_pulse_width=self.calibParam["minPWM"], max_pulse_width=self.calibParam["maxPWM"])
        self.servo.detach()


# --------------------- Config -------------------------

    def configServo(self, newCalibParam):
        self.calibParam = newCalibParam
        self.servo = AngularServo(self.calibParam["port"], min_angle=self.calibParam["mini_angle"], max_angle=self.calibParam["maxi_angle"], min_pulse_width=self.calibParam["minPWM"], max_pulse_width=self.calibParam["maxPWM"])


# --------------------- Rotation -------------------------
        
    def rotateDirect(self, angle):
        print(angle)
        self.servo.angle = angle
        self.angle = self.servo.angle
        self.fileControler.writePartPartFile("servo", "angle", self.servo.angle)
        sleep(0.5)
        self.servo.detach()
        
    def rotateSlow(self, angle):
        self.servo.angle = self.angle
        print(self.fileControler.readFile()["servo"]["status"])
        while self.fileControler.readFile()["servo"]["status"] == "continu" and (angle == 1 or self.servo.angle > 0.0) and (angle == -1 or self.servo.angle < 180.0):
            self.servo.angle = self.servo.angle + (angle * self.speed)
        sleep(0.5)
        self.angle = self.servo.angle
        self.fileControler.writePartPartFile("servo", "angle", self.servo.angle)
        self.servo.detach()

    
