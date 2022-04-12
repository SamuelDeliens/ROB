# ------------------------------------------------------    
# --------------------- Measure Sensor -----------------
# ------------------------------------------------------

from MCP3008 import MCP3008

offsetPH = 0.40
average = 100.0
adc = MCP3008()

# --------------------- Config -------------------------

def configMesure(_offsetPH, _average, _adc):
    global offsetPH, average, adc
    offsetPH = _offsetPH
    average = _average
    adc = _adc
   
# --------------------- Compo -------------------------

#Get average value
def doAverage(pin):
    global average
    mValue = 0.0
    for i in range(int(average)):
        value = adc.read( channel = (pin) )
        time.sleep((0.1 / average))
        mValue = mValue + (value / average)
    return mValue

#get measures
def measureVoltage(outA):
    for pin in range(3):
        mValue = doAverage(pin)
        voltage = mValue / 1023.0 *3.3
        outA[pin] = voltage
    return  outA

#convert Analogique to Numerique
def convert(outA):
    global offset
    outA[0] = 3.5 * outA[0] + offset
    outA[1] = outA[1]
    outA[2] = outA[2]
    return  outA

# --------------------- Measure -------------------------

def measure():
    outA = [0, 0, 0]
    outA = measureVoltage(outA)        
    outA = convert(outA)
    return  outA
