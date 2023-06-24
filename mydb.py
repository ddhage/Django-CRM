import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123'
)
#prepare a cursor object
cursorObj = dataBase.cursor()

#create a db

cursorObj.execute("CREATE DATABASE elderco")

print("Database created")
