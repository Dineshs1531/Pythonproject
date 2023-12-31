# import mysql.connector
# from mysql.connector import Error
from existing_account import *
# import random
import re
from datetime import datetime,date
#pip install bcrypt

import bcrypt

from sql import *

""""-------------------------------------- SQL CONNECTING ----------------------------------SATRT"""
# put our mysql terminal password

password = 'Dinesh1531@'

# Databasename
database_name = 'bank'

# create database in mysql




# creating table as user details from  BANK DATABASE





# query for creating the table in Bank database

create_user_details = """
CREATE TABLE USER_DETAILS(
ACCOUNT_NUMBER INT PRIMARY KEY,
IFSC_CODE VARCHAR(10) NOT NULL,
AMOUNT DECIMAL NOT NULL,
ACCOUNT_HOLDER_NAME VARCHAR(50) NOT NULL,
EMAIL VARCHAR(30),
PHONE_NUMBER VARCHAR(10) CHECK(LENGTH(PHONE_NUMBER)=10),
DOB VARCHAR(20) CHECK(LENGTH(DOB)=10) NOT NULL,
ADDRESS VARCHAR(50) NOT NULL,
ANDHARNUMBER VARCHAR(20) CHECK(LENGTH(ANDHARNUMBER)=12),
PANCARD_NUMBER VARCHAR(20) CHECK(LENGTH(PANCARD_NUMBER)=10));
"""
create_credit_card_details="""
CREATE TABLE CREDIT_CARD_DETAILS(
AC BIGINT,
CREDIT_CARD_NUMBER BIGINT UNIQUE,
VAILD_FROM DATE,
VAILD_UP DATE,
PIN VARCHAR(1000),
FOREIGN KEY(AC) REFERENCES user_details(ACCOUNT_NUMBER));"""
# connection to the database

connection = create_server_connection("localhost", "root", password, database_name)


# creating table using python that query executed
# execute_query(connection,create_user_details)
# execute_query(connection,create_credit_card_details,message="created")



# ---------------------------------   READ QUERY EXECUTED ---------------------




"""" ----------------------------------- SQL CONNECTING END ------------------------------------------ """

""" ---------------------------- NEW ACCOUNT CREATING ---------------------------------------- """


def new_account_created(ac):
    Bank_name = 'Canara Bank'
    # Branch = 'Thalaivasal'
    IFSC = 'CNR91002'

    def user_details():

        l = ['AMOUNT', 'ACCOUNT_HOLDER_NAME', 'EMAIL', 'PHONE_NUMBER', 'DOB', 'ADDRESS',
             'ANDHARNUMBER', 'PANCARD_NUMBER']
        pattern = [r'^\d{4,}$', r'^[A-Za-z\s]+$',
                   r'((^[a-z]{1,})+([._-])?([a-z])?([0-9]{1,})+(@gmail.com$))|((^[a-z]{1,})+(@)+([^gmail.com])+([a-z]{1,})+(.)+([a-z]{1,}$))',
                   r'^\d{10}$', r'^(0[1-9]|[12][0-9]|[3][01])-(0[1-9]|1[0-2])-(19|20[0-9]{2})',
                   r'^[A-Za-z0-9 .-/(),_]+$', r'^\d{12}$', r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$']

        def add_userdetails():
            value = []
            value.extend([ac, IFSC])
            for i, j in zip(l, pattern):
                while True:
                    input_value = input(f"Enter the {i} : ")
                    if re.match(j, input_value):
                        value.append(input_value)
                        break
                    else:
                        print(f"please enter the valid {i}")

            #to change string to mysql date format
            date_string=value[6]

            date_object = datetime.strptime(date_string, '%d-%m-%Y')
            mysql_date=date_object.strftime('%Y-%m-%d')
            value[6]=mysql_date
            # print(value[6])
            print("please wait for few seconds your request puropse going on  ......")
            time.sleep(4)
            inserting_datas = f"""
                    insert into user_details (ACCOUNT_NUMBER,IFSC_CODE,AMOUNT,ACCOUNT_HOLDER_NAME,EMAIL,
                    PHONE_NUMBER,DOB,ADDRESS,ANDHARNUMBER,PANCARD_NUMBER) values
                    ({int(value[0])},'{value[1]}',{int(value[2])},'{value[3]}','{value[4]}',
                    '{value[5]}',STR_TO_DATE('{mysql_date}','%Y-%m-%d'),'{value[7]}','{value[8]}','{value[9]}');"""
            execute_query(connection, inserting_datas,message=f"Account is created successfully and your account_number is {int(value[0])},current_balance is {int(value[2])}")

        add_userdetails()

    user_details()


"""----------------------------- BANK OPERATIONS ----------------------------------------"""


def existing_account(connection,ac):

    while True:
        l = ['Check_balance','Deposit_amount', 'Writhdraw_amount','Apply for Debit card','Apply for Credit card']
        c = 1
        for i in l:
            print(f"{c}.{i}")
            c += 1
        choose = input("Enter the choose option : ")
        match int(choose):
            case 1:
                check_balance(connection,ac)
            case 2:
                deposit(connection,ac)
            case 3:
                writhdraw(connection,ac)
            case 4:
                apply_debit_card(connection, ac)
            case 5:
                apply_credit_card(connection,ac)
            case _:
                print('Please enter valid option : ')
        continue1 = input("DO YOU WANT TO CONTINUE (YES/NO)")
        if continue1[0].lower() == 'n':
            break


"""----------------------------- ACCOUNT NUMBER GENERATOR ----------------------------------------------------------------"""


def account_number_generator():
    acc=0
    try:
        query = """SELECT MAX(ACCOUNT_NUMBER) FROM USER_DETAILS;"""
        result = read_query(connection, query)
        acc = result[0][0]
        return acc+1
    except:
        return 632240183001
    # return ac+1


ac = account_number_generator()

"""----------------------------------------- STARTING WITH -----------------------------------------------------------"""
# id=1
while True:
    print("\n***  WELCOME TO CANARA BANK  ***")
    li = ['New account creating', 'Existing account']
    c = 1

    for i in li:
        print(f'{c}.{i}')
        c += 1
    entering = input("choose your optional : ")
    if entering.isdigit():
        entering = int(entering)
        match entering:
            case 1:
                new_account_created(ac)


            case 2:
                while True:

                    try:
                        ac = int(input("Enter the account number : "))
                        res = []
                        query_account_numbers = """select ACCOUNT_NUMBER FROM USER_DETAILS;"""
                        account_numbers = read_query(connection, query_account_numbers)
                        for i in account_numbers:
                            res.append(i[0])
                        if ac in res:
                            existing_account(connection,ac)
                            res.clear()
                            break
                        else:
                            print("enter the vaild account number !")
                        break
                    except ValueError:
                        print("Please enter the valid account number (not in integer)  ")



            case _:
                print("please the valid information")
    else:
        print("please enter the digits")
    # print(account_holder_details)

    continue1 = input("Do you want to continue (yes/no) : ")
    if continue1[0].lower() == 'n':
        break


