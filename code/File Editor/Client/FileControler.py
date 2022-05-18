#------------------------------------------------------
#-------------------- File Controler ------------------
#------------------------------------------------------

import json

class FileControler:
    
    def __init__(self):
        self.pathFile = "../python/data.json"        

#----------------------- Controler ---------------------

    def writeFile(self, status):
        file = open(self.pathFile, 'w')
        json.dump(status, file, indent=6)
        file.close()
    
    def readFile(self):
        file = open(self.pathFile, 'r')
        status = json.load(file)
        file.close()
        return status
    
    def writeStatus(self, typeS, newStatus):
        status = self.readFile()
        status[typeS]["status"] = newStatus
        self.writeFile(status)