# ------------------------------------------------------    
# ---------------------- Actioner ----------------------
# ------------------------------------------------------

from Sensor import Sensor
from ServoMotor import ServoMotor
from Camera import Camera

class Actioner:
    """Static class Actioner
        Get same sensor, servo and camera
    """
    sensor = Sensor()
    servo = ServoMotor()
    camera = Camera()