# ------------------------------------------------------    
# ---------------------- Actioner ----------------------
# ------------------------------------------------------

from Sensor import Sensor
from ServoMotor import ServoMotor

class Actioner:
    """Static class Actioner
        Get same sensor and servo
    """
    sensor = Sensor()
    servo = ServoMotor()