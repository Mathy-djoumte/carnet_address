import mysql.connector

config = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="contacts"
)


def ajouter_contact(name, firstname, phone):
    cursor = config.cursor()

    insert = "INSERT INTO user (name, firstname, phone) VALUES (%s, %s, %s)"
    values = (name, firstname, int(phone))
    cursor.execute(insert, values)
    config.commit()

    print(cursor.rowcount, "details inserted")
    cursor.close()


print("succeed")
