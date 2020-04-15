import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='')

        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")

        databases = cursor.fetchall()
        dbName = None

        for db in databases:
            if db[0] == "proj_emerging_tech":
                dbName = "proj_emerging_tech"
                break

        if dbName is not None:
            connection = mysql.connector.connect(host='localhost', user='root', password='', database=dbName)
        else:
            create_db()

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "Error while connecting to MySQL"

    finally:
        if connection.is_connected():
            version = connection.get_server_info()
            print("Connected to MySQL Server version ", version)


def create_db():
    connection = mysql.connector.connect(host='localhost', user='root', password='')
    try:
        # create database
        db_cursor = connection.cursor()
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS proj_emerging_tech")

    except Error as e:
        print("Error while creating database to MySQL", e)
        return "Error while creating database"

    finally:
        if connection.is_connected():
            create_tables()
            db_cursor.close()
            connection.close()
            print("Database created")


def create_tables():
    connection = mysql.connector.connect(host='localhost', user='root', password='', database="proj_emerging_tech")
    try:
        cursor = connection.cursor()
        # create tables
        cursor.execute("CREATE TABLE IF NOT EXISTS User (userId int(11) PRIMARY KEY," +
                       " username varchar(45) DEFAULT NULL," +
                       " password varchar(45) DEFAULT NULL," +
                       " type varchar(45) DEFAULT NULL)")

        cursor.execute("CREATE TABLE IF NOT EXISTS Course (courseCode varchar(5) PRIMARY KEY," +
                       " courseName varchar(45) DEFAULT NULL)")

        cursor.execute("CREATE TABLE IF NOT EXISTS Professor (" +
                       " idProf int(11) NOT NULL," +
                       " courseCodeProf varchar(45) NOT NULL," +
                       " nameProf varchar(45) DEFAULT NULL," +
                       " userIdProf int(11) DEFAULT NULL," +
                       " PRIMARY KEY (idProf,courseCodeProf)," +
                       " KEY courseCode_idx (courseCodeProf)," +
                       " KEY userIdProf_idx (userIdProf)," +
                       " CONSTRAINT courseCodeProf FOREIGN KEY (courseCodeProf) REFERENCES Course (courseCode)," +
                       " CONSTRAINT userIdProf FOREIGN KEY (userIdProf) REFERENCES User (userId))")

        cursor.execute("CREATE TABLE IF NOT EXISTS Student (" +
                       " idStudents int(11) NOT NULL," +
                       " studentName varchar(45) DEFAULT NULL," +
                       " courseCodeStd varchar(45) NOT NULL," +
                       " grade int(11) DEFAULT NULL," +
                       " userIdStd int(11) DEFAULT NULL," +
                       " profIdStd int(11) DEFAULT NULL," +
                       " PRIMARY KEY (idStudents, courseCodeStd)," +
                       " KEY courseCodeStd_idx (courseCodeStd)," +
                       " KEY userIdStd_idx (userIdStd)," +
                       " KEY profIdStd_idx (profIdStd)," +
                       " CONSTRAINT courseCodeStd FOREIGN KEY (courseCodeStd) REFERENCES course (courseCode)," +
                       " CONSTRAINT profIdStd FOREIGN KEY (profIdStd) REFERENCES professor (idProf)," +
                       " CONSTRAINT userIdStd FOREIGN KEY (userIdStd) REFERENCES user (userId))")

        # Insert adm user in table
        cursor.execute("INSERT IGNORE INTO User (userId, username, password, type)" +
                       " VALUES (00001, 'adm', 1234, 'ADM')")

        connection.commit()

    except Error as e:
        print("Error while creating tables to MySQL", e)
        return "Error while creating tables"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("tables created")
