import mysql.connector
from mysql.connector import Error

class DataBaseConnection():
    def __init__(self):

    def connect(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='project',
                                                 user='root',
                                                 password='')
            if connection.is_connected():
                version = connection.get_server_info()
                print("Connected to MySQL Server version ", version)
                cursor = connection.cursor()
                cursor.execute("select database();")
                schema = cursor.fetchone()
                print("Connected to database: ", schema)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Connection is closed")