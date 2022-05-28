# ------------------------------------------------------    
# ---------------------- Actioner ----------------------
# ------------------------------------------------------

from Sensor import Sensor
from ServoMotor import ServoMotor
from Camera import Camera

class Actioner:
    sensor = Sensor()
    servo = ServoMotor()
    camera = Camera()