import pymysql.cursors

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

def deleteValue():
    connection = connectionBDD()
    with connection.cursor() as cursor:
        sql= "DELETE FROM capteur"
        cursor.execute(sql)
        reponse = cursor.fetchall()
    connection = closeBDD(connection)
    
deleteValue()