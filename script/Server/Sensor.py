# ------------------------------------------------------    
# --------------------- Measure Sensor -----------------
# ------------------------------------------------------

import time

from MCP3008 import MCP3008
from FileControler import FileControler

class Sensor:
    """object sensors 
    get the sensor values
    """
    def __init__(self):
        """Contructor
        define sensor with default parameter
        """
        self.average = 100.0
        self.temperature= 25.0
        self.configPoint = {"pH": {"neutralVoltage": 1500.0,"acidVoltage": 2032.44}, "oxygen": {"oxyvaluelow": 1300,"oxyvalueHigh": 1600},"conductivity": {"kvaluelow": 1.0,"kvalueHigh": 1.0}}
        self.kvalue= 1.0
        self.oxygenTable = [14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11010, 11530, 11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270, 9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690, 7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410]
        self.adc = MCP3008()
        self.configSensor(100.0)


# --------------------- Config -------------------------

    def configSensor(self, _average):
        """configure the sensor

        Args:
            _average (int): number of value get before to average
        """
        self.average = _average
        self.configPoint = FileControler.readFile()["sensor"]

# --------------------- Compo -------------------------

#Get average value
    def doAverage(self, pin):
        """get multiple value to average

        Args:
            pin (int): which sensor to get value

        Returns:
            int: value get by the sensor
        """
        mValue = 0.0
        for i in range(int(self.average)):
            value = self.adc.read( channel = (pin) )
            time.sleep((0.1 / self.average))
            mValue = mValue + (value / self.average)
        return mValue
    
#get measures
    def measureVoltage(self, outA):
        """transform sensor value to voltage

        Args:
            outA (array): array of voltage value of sensors

        Returns:
            array: same array with voltage value
        """
        for pin in range(3):
            mValue = self.doAverage(pin)
            voltage = mValue / 1023.0 *3.3
            outA[pin] = voltage
        return  outA

# --------------------- Calibrate -----------------------
    
    def waitStabilisation(self, pin):
        """calibrate function to wait till the value is stable

        Args:
            pin (int): pin of the sensor calibrate

        Returns:
            int: value of the calibration
        """
        mValue = self.doAverage(pin)
        i=0
        while i<5 :
            time.sleep(0.5)
            newMValue = self.doAverage(0)
            if (abs(round(mValue, 2) - round(newMValue, 2)) < 0.1):
                i=i+1
            else:
                i=0
                mValue = newMValue
        return mValue
    
    def calibratePH(self, step):
        """calibration of the pH sensor

        Args:
            step (int): step of the calibration (1 or 2)

        Returns:
            str: Done
        """
        mValue = self.waitStabilisation(0)
        voltage = mValue / 1023.0 *3.3
        if (step == 0):
            self.neutralVoltage = voltage 
        else:
            self.acidVoltage = voltage
        FileControler.writePartFile("sensor", self.configPoint)
        return "Done"
    
    def calibrateOxygen(self, step):
        """calibration of the oxygen sensor

        Args:
            step (int): step of the calibration (1 or 2)

        Returns:
            str: Done
        """
        mValue = self.waitStabilisation(1)
        voltage = mValue / 1023.0 *3.3
        if (step == 0):
            self.oxyvaluelow = voltage
        else:
             self.oxyvalueHigh = voltage
        FileControler.writePartFile("sensor", self.configPoint)
        return "Done"
             
    def calibrateConductivity(self, step):
        """calibration of the conductivity sensor

        Args:
            step (int): step of the calibration (1 or 2)

        Returns:
            str: Done
        """
        mValue = self.waitStabilisation(2)
        voltage = mValue / 1023.0 *3.3
        if (step == 0):
            valueTemp = 820.0*200.0*1.413/1000.0/voltage
            self.kvaluelow = valueTemp
        else:
            valueTemp = 820.0*200.0*12.88/1000.0/voltage
            self.kvalueHigh =  valueTemp
        FileControler.writePartFile("sensor", self.configPoint)
        return "Done"
  
  
# --------------------- Convert -------------------------

#convert ph
    def convertPH(self, voltage):
        """conversion voltage to pH

        Args:
            voltage (int): voltage value of the sensor

        Returns:
            int: return the pH value
        """
        slop = (7.0-4.0)/((self.configPoint["pH"]["neutralVoltage"]-1500.0)/3.0 - (self.configPoint["pH"]["acidVoltage"]-1500.0)/3.0)
        intercept = 7.0 - slop*(self.configPoint["pH"]["neutralVoltage"]-1500.0)/3.0
        value = slop*(voltage-1500.0)/3.0+intercept
        return value
    
#convert Conductivity
    def convertConductivity(self, voltage):
        """conversion voltage to ms

        Args:
            voltage (int): voltage value of the sensor

        Returns:
            int: return the conductivity value
        """
        rawEC = 1000*voltage/820.0/200.0
        valueTemp = rawEC
        if (valueTemp > 2.5):
            kvalue = self.configPoint["conductivity"]["kvalueHigh"] #High Value Calibration
        elif(valueTemp < 2.0):
            kvalue = self.configPoint["conductivity"]["kvaluelow"] #Low Value Calibration
        value = rawEC * kvalue
        #value =  value / (1.0+0.0185*(self.temperature-25))
        return value
    
#convert Oxygen
    def convertOxygen(self, voltage):
        """conversion voltage to oxygen

        Args:
            voltage (int): voltage value of the sensor

        Returns:
            int: return the oxygen value
        """
        saturation = (self.temperature - 15) * (self.configPoint["oxygen"]["oxyvalueHigh"] - self.configPoint["oxygen"]["oxyvaluelow"]) / (25 - 15) + self.configPoint["oxygen"]["oxyvaluelow"]
        value = voltage * self.oxygenTable[round(self.temperature)] / saturation
        return value


#convert Analogique to Numerique
    def convert(self, outA):
        """conversion of the three value

        Args:
            outA (array): array of voltage values

        Returns:
            array: array of convert values
        """
        outA[0] = self.convertPH(outA[0])
        outA[1] = self.convertConductivity(outA[1])
        outA[2] = self.convertOxygen(outA[2])
        return  outA


# --------------------- Measure -------------------------

    def measures(self):
        """get value of the sensors

        Returns:
            array: each value of sensors
        """
        outA = [0, 0, 0]
        outA = self.measureVoltage(outA)        
        outA = self.convert(outA)
        return  outA