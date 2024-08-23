import mysql.connector

config= mysql.connector.connect(
    host="localhost",
    username= "root",
    password="",
)
#create cusor
cusor = config.cursor()
cusor.execute("CREATE DATABASE contact")







