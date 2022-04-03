from MCP3008 import MCP3008


adc = MCP3008()
valeur = adc.read( channel = 0 )
print("Appleid voltage: %.2f" % (valeur / 1023.0 * 3.3))

import time
from MCP3008 import MCP3008

offset = 0.40
moyenne = 100.0
adc = MCP3008()
while 1:
        mValue = 0.0
        for i in range(int(moyenne)):
                value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out
                time.sleep((1 / moyenne))
                mValue = mValue + (value / moyenne)
        voltage = mValue / 1023.0 *3.3
        pH = 3.5 * voltage + offset
        print("Applied pH: %.2f" % pH )
        print("Applied voltage: %.2f" % voltage )





