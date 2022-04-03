import pymysql.cursors

connection= pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= 'pi',
    database= 'Rob',
)

with connection.cursor() as cursor:
	sql= "SELECT id,date,pH FROM capteur WHERE id = 1"
	select = 1
	cursor.execute(sql)
	result = cursor.fetchall()
	print(result)


connection.close()
