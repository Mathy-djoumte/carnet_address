import mysql.connector

config = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="contacts"
)

connect = config.cursor()

user = """
    CREATE TABLE user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        phone VARCHAR(15) NOT NULL
    )
"""
connect.execute(user)
config.close()
