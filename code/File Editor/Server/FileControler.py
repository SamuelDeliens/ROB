import json

class FileControler :
    def __init__(self):
        self.PathFile = "data.json"
        
#-----------------controler----------------------

    def writeFile(self, data):
        file = open(self.PathFile, 'w')
        json.dump(data,file)
        file.close()
        
    def readFile(self):
        file = open(self.PathFile, 'r')
        data = json.load(file)
        file.close()
        return data