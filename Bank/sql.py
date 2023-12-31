import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, database_name):
    connection = None

    # error handling
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        )
        print("Mysql Database connection successfully")
    except Error as er:
        print(f'Error : {er}')
    return connection


"""def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("DATABASE CREATE SUCCESSFULLY ")
    except Error as er:
        print(f'Error : {er}')


create_database_query = "CREATE DATABASE BANK"
# create_database(connection,create_database_query)
"""
def execute_query(connection, query,message):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(message)
    except Error as er:
        print(f'Error : {er}')


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as er:
        print(f"ERROR : {er}")