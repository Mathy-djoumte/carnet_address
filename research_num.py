import mysql.connector

def research_data(num):

    config = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="contacts"
    )

    cursor = config.cursor()
    search = "SELECT * FROM user WHERE id = %s"
    cursor.execute(search, (num,))

    result = cursor.fetchone()

    config.close()

    return result
