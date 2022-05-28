#------------------------------------------------------
#-------------------- File Controler ------------------
#------------------------------------------------------

import json

class FileControler :
    """object pemit to touch data saved in file
    """
    pathFile = "/home/pi/Desktop/ROB/Server/data.json"


#-----------------controler----------------------
    
    @classmethod 
    def writeFile(cls, data):
        """change the data file
        
        Args:
            data (str): new data to save
        """
        file = open(cls.pathFile, 'w')
        json.dump(data,file)
        file.close()
    
    @classmethod
    def readFile(cls):
        """read the data file
        
        Returns:
            str: data in the file
        """
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
        """write a part in the json data
        
        Args:
            part (str): the part to write
            data (str): new data to save
        """
        allData = cls.readFile()
        allData[part] = data
        cls.writeFile(allData)
        
    @classmethod
    def writePartPartFile(cls, part1, part2, data):
        """write a part of a part in the json data
        
        Args:
            part1 (str): the first part to write
            part2 (str): the secon part to write
            data (str): new data to save
        """
        allData = cls.readFile()
        allData[part1][part2] = data
        cls.writeFile(allData)