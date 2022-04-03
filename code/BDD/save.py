from MCP3008 import MCP3008
import pymysql.cursors
import time
import datetime

offset = 0.40
moyenne = 100.0
adc = MCP3008()
mValue = 0.0

for i in range(int(moyenne)):
	value = adc.read( channel = 0 )
	time.sleep((0.1 / moyenne))
	mValue = mValue + (value / moyenne)
voltage = mValue / 1023.0 *3.3
pHvalue = 3.5 * voltage + offset

print("Applied pH: %.2f" % pHvalue )

connection= pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= 'pi',
    database= 'Rob',
)

with connection.cursor() as cursor:
        sql= "INSERT INTO capteur (date,pH) VALUES (%s,%s)"
        cursor.execute(sql, (datetime.datetime.today(), pHvalue))
        #cursor.execute("INSERT INTO capteur (date, pH) VALUES (NOW(), 7.5)")

connection.commit()

with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM capteur")
        result = cursor.fetchall()
        print(result)

connection.close()
