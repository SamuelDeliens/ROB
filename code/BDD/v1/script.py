import Save
import initBDD
from MCP3008 import MCP3008

    # ============================================================
    # Script
    # ============================================================

offset = 0.40
moyenne = 100.0
adc = MCP3008()
accuracy = 3

#initBDD.deleteValue()
#Save.config(adc, offset, moyenne, accuracy)
#Save.getMuchMesure()