#------------------------------------------------------
#-------------------- File Controler ------------------
#------------------------------------------------------

class FileControler:
    
    def __init__(self):
        self.pathFile = "../python/data.txt"

#----------------------- Controler ---------------------

    def writeFile(self, status):
        file = open(self.pathFile, 'w')
        file.write(status)
        file.close()
    
    def readFile(self):
        file = open(self.pathFile, 'r')
        status = file.read()
        file.close()
        return status        