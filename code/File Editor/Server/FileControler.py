import json

class FileControler :
    pathFile = "data.json"


#-----------------controler----------------------
    
    @classmethod 
    def writeFile(cls, data):
        file = open(cls.pathFile, 'w')
        json.dump(data,file)
        file.close()
    
    @classmethod
    def readFile(cls):
        file = open(cls.pathFile, 'r')
        try:
            if file == None or file == '':
                data = "Error"
            else:
                read = file.read()
                if read == None or read == '':
                    data = "Error"
                else:
                    data = json.loads(read)
        except:
            print("reading file error")
            data = "Error"
        file.close()
        return data


#-----------------WRITING PART----------------------
    
    @classmethod
    def writePartFile(cls, part, data):
        allData = cls.readFile()
        allData[part] = data
        cls.writeFile(allData)
        
    @classmethod
    def writePartPartFile(cls, part1, part2, data):
        allData = cls.readFile()
        allData[part1][part2] = data
        cls.writeFile(allData)