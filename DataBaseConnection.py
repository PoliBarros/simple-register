import mysql.connector


def connect():
    connection = mysql.connector.connect(host='localhost', database='project', user='root', password='')

    if connection.is_connected():
        version = connection.get_server_info()
        print("Connected to MySQL Server version ", version)
        return connection
