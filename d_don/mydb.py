import mysql.connector
import pymysql



database = mysql.connector.connect(
    host = 'localhost',
    user = 'dali',
    passwd = 'DAli@@1997@@',
)

#prepare a cursor object


cursorObject = database.cursor()


#create a database 

cursorObject.execute("CREATE DATABASE donation ")
print ("All done !")