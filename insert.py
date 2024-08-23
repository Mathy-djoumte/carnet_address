import mysql.connector

config = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="contacts"
)

cusor= config.cursor()

insert= "INSERT INTO user (name, firstname,phone) VALUES ('Mathilde', 'Mathy', '658791221')"


cusor.execute(insert)
config.commit()
print(cusor.rowcount, "details inserted")
config.close()