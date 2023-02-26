import mysql.connector
from mysql.connector import Error
import pyodbc

class Sql_connection:
    def Get_connection(self):
        connection_string='DRIVER={SQL Server};SERVER=80.78.240.16;DATABASE=Qwerty;UID=student;PWD=qwe!23'
        connection = None
        try:
            connection = pyodbc.connect(connection_string)
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def Get_from_db(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
        return result

    def DoSmfng(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")