#------------------------------------------------------
#-------------------- File Controler ------------------
#------------------------------------------------------

import json

class FileControler:
    """object pemit to touch data saved in file
    """
    def __init__(self):
        self.pathFile = "../python/data.json"        

#----------------------- Controler ---------------------

    def writeFile(self, status):
        """change the data file

        Args:
            status (str): new status to save
        """
        file = open(self.pathFile, 'w')
        json.dump(status, file, indent=6)
        file.close()
    
    def readFile(self):
        """read the data file

        Returns:
            str: status in the file
        """
        file = open(self.pathFile, 'r')
        status = json.load(file)
        file.close()
        return status
    
    def writeStatus(self, typeS, newStatus):
        """write a part in the json data

        Args:
            typeS (str): the part to write
            newStatus (str): new status to save
        """
        status = self.readFile()
        status[typeS]["status"] = newStatus
        self.writeFile(status)