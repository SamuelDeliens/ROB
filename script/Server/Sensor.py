# ------------------------------------------------------    
# --------------------- Measure Sensor -----------------
# ------------------------------------------------------

import time

from MCP3008 import MCP3008

class Sensor:

    def __init__(self):
        self.offsetPH = 0.40
        self.average = 100.0
        self.kvalue= 1.0
        self.temperature= 25.0
        self.saturation= 2.29
        self.oxygenTable = [14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11010, 11530, 11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270, 9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690, 7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410]
        self.adc = MCP3008()


# --------------------- Config -------------------------

    def configSensor(self, _offsetPH, _average):
        self.offsetPH = _offsetPH
        self.average = _average
   
   
# --------------------- Compo -------------------------

#Get average value
    def doAverage(self, pin):
        mValue = 0.0
        for i in range(int(self.average)):
            value = self.adc.read( channel = (pin) )
            time.sleep((0.1 / self.average))
            mValue = mValue + (value / self.average)
        return mValue
    
#get measures
    def measureVoltage(self, outA):
        for pin in range(3):
            mValue = self.doAverage(pin)
            voltage = mValue / 1023.0 *3.3
            outA[pin] = voltage
        return  outA

# --------------------- Convert -------------------------

#convert Conductivity
    def convertConductivity(self, voltage):
        rawEC = 1000*voltage/820.0/200.0
        valueTemp = rawEC
        if (valueTemp > 2.5):
            kvalue = 1.14 #High Value Calibration
        elif(valueTemp < 2.0):
            kvalue = 1.16 #Low Value Calibration
        value = rawEC * kvalue
        value =  value / (1.0+0.0185*(self.temperature-25))
        return value
    
#convert Oxygen
    def convertOxygen(self, voltage):
        saturation = (self.temperature - 15) * (1600 - 1300) / (25 - 15) + 1300 
        value = voltage * oxygenTable[self.temperature] / saturation
        return value


#convert Analogique to Numerique
    def convert(self, outA):
        outA[0] = 3.5 * outA[0] + self.offsetPH
        outA[1] = self.convertConductivity(outA[1])
        outA[2] = self.convertOxygen(outA[2])
        return  outA


# --------------------- Measure -------------------------

    def measures(self):
        outA = [0, 0, 0]
        outA = self.measureVoltage(outA)        
        outA = self.convert(outA)
        return  outA