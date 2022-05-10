# ------------------------------------------------------    
# --------------------- Measure Sensor -----------------
# ------------------------------------------------------

import time
from MCP3008 import MCP3008

class Sensor:

    def __init__(self):
        self.offsetPH = 0.40
        self.kvaluelow= 1.0
        self.kvaluehigh= 1.0
        self.kvalue= 1.0
        self.temperature= 25.0
        self.saturation= 3.43
        self.average = 100.0
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
#readEC
    def readEC(self,voltage):
        rawEC = 1000*voltage/820.0/200.0
        valueTemp = rawEC* self.kvalue
        if(valueTemp > 2.5):
            self.kvalue= self.kvaluehigh
        elif(valueTemp < 2.0):
            self.kvalue= self.kvaluelow
        valueEC = rawEC * self.kvalue
        valueEC = valueEC / (1.0+0.0185*(self.temperature-25.0))
        return valueEC

        
                
#convert Analogique to Numerique
    def convert(self, outA):
        outA[0] = 3.5 * outA[0] + self.offsetPH
        outA[1] =  readEC(outA[1])
        outA[2] = outA[2]*8410/self.saturation
        return  outA

# --------------------- Measure -------------------------

    def measures(self):
        outA = [0, 0, 0]
        outA = self.measureVoltage(outA)        
        outA = self.convert(outA)
        return  outA
