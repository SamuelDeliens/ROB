from MCP3008 import MCP3008
import pymysql.cursors
import time
import datetime

offset = 0.40
moyenne = 100.0
adc = MCP3008()
accuracy = 1

    # ============================================================
    # Fonction
    # ============================================================

def config(adc, offset, moyenne, accuracy):
    offset = offset
    moyenne = moyenne
    adc = adc
    accuracy = accuracy

    # ------------------MESURE ---------------------

def doMoyenne(pin, moyenne):
    mValue = 0.0
    for i in range(int(moyenne)):
        value = adc.read( channel = (pin) )
        time.sleep((0.1 / moyenne))
        mValue = mValue + (value / moyenne)
    return mValue

def mesureVoltage(sortieA):
    for pin in range(3):
        mValue = doMoyenne(pin, moyenne)
        voltage = mValue / 1023.0 *3.3
        sortieA[pin] = voltage
    return  sortieA

def conversionValeur(sortieA):
    sortieA[0] = 3.5 * sortieA[0] + offset
    sortieA[1] = sortieA[1]
    sortieA[2] = sortieA[2]
    return  sortieA

def mesure():
    sortieA = [0, 0, 0]
    sortieA = mesureVoltage(sortieA)        
    sortieA = conversionValeur(sortieA)
    return  sortieA

    # ------------------BDD ---------------------

def connectionBDD():
    connection= pymysql.connect(
        host= 'localhost',
        user= 'root',
        password= 'pi',
        database= 'Rob',
    )
    return connection

def closeBDD(connection):
    connection.commit()
    connection.close()
    return connection

def inssertBDD(sortieA):
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "INSERT INTO capteur (date,pH,oxygen,conductivity) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (datetime.datetime.today(), sortieA[0], sortieA[1], sortieA[2]))
    connection = closeBDD(connection)
        
def getBDD():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "SELECT * FROM capteur"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    print(reponse)

def getLastRow():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "SELECT * FROM capteur ORDER BY id DESC LIMIT 0,1"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    return reponse

def checkIfChange(sortieA):
    lastRow = getLastRow()
    if (lastRow != ()):
        lastRow = lastRow[0]
        difference = False
        for i in range(len(lastRow)-2):
            print(lastRow[i+2])
            print(sortieA[i])
            if (round(lastRow[i+2],accuracy) != round(sortieA[i],accuracy)):
                difference = True
    else:
        difference = True
    return difference

def getMuchMesure():
    nb = 0
    while (nb < 10):
        nb = nb+0  
        newValue = mesure()
        if (checkIfChange(newValue) == True):
            print("change")
            inssertBDD(newValue)
            
    # ============================================================
    # Script
    # ============================================================

offset = 0.40
moyenne = 100.0
adc = MCP3008()
accuracy = 2

#initBDD.deleteValue()
config(adc, offset, moyenne, accuracy)
print(bytearray(str(getLastRow()), 'utf-8'))
#getMuchMesure()            