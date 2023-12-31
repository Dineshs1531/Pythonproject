import bcrypt
from sql import *
import random,time
from datetime import datetime,date

"""-----------------------------------DEPOSIT AMOUNT-------------------------------------------------"""


def account(connection,ac):
    query_for_amount_taken_particular_user = f"""SELECT AMOUNT FROM USER_DETAILS WHERE ACCOUNT_NUMBER={ac};"""
    current_amount = read_query(connection, query_for_amount_taken_particular_user)
    # print(current_amount[0][0]) O/P -> 1000.0
    return current_amount[0][0]

def check_balance(connection,ac):
    current_balance = account(connection,ac)
    print("please wait for few seconds your balance checking ......")
    time.sleep(4)
    print(f"YOUR ACCOUNT AVAIABLE BALANCE : {current_balance}")

    """------------ deposit----------------"""
def deposit(connection,ac):
     while True:
         try:
            deposit_amount = int(input("enter the deposite amount : "))
            current_balance = account(connection,ac)
            query_for_update_amount = f"""UPDATE USER_DETAILS SET AMOUNT={deposit_amount + current_balance} WHERE ACCOUNT_NUMBER={ac}"""
            execute_query(connection, query_for_update_amount,message=f"Your amount is successfully deposited and your current_balance is {deposit_amount + current_balance}")
            break
         except ValueError:
             print("please enter valid amount|")


"""------------------------------------------- WITHDRAW---------------------------------------------------------------"""

def writhdraw(connection,ac):
    while True:
        try:
            writhdaw_amount = int(input("enter the writhdraw amount : "))
            current_balance = account(connection,ac)
            if current_balance >=1 and writhdaw_amount <= current_balance:
                query_for_update_amount = f"""UPDATE USER_DETAILS SET AMOUNT={current_balance - writhdaw_amount} WHERE ACCOUNT_NUMBER={ac}"""
                print("please wait for few seconds your withdraw process going on  ......")
                time.sleep(4)
                execute_query(connection, query_for_update_amount,message=f"Your amount is successfully writhdraw and your current_balance is {current_balance - writhdaw_amount}")
                break
            else:
                print("Your account balance is insufficient ! ")
                print('try again , and please enter the valid amount')
                break
        except ValueError:
            print("please enter the amount !")
        except not ValueError:
            print("please enter the valid amount!")

def apply_debit_card(connection,ac):

    # to check already debit is or not
    # print("apply debit")
    #to checking in user_details table
    checking_debit_card_query = f"""SELECT DEBIT_CARD_NUMBER FROM USER_DETAILS Where ACCOUNT_NUMBER={ac};"""
    checking_is_present = read_query(connection, checking_debit_card_query)
    # print("checking_is_present : ", checking_is_present)

    #debit_card_detail table checking
    checking_debit_card_query1 = f"""SELECT AC FROM DEBIT_CARD_DETAILS Where AC={ac};"""
    checking_is_present1 = read_query(connection, checking_debit_card_query1)
    # print("checking_is_present : ", checking_is_present1)

    # [(None,)]
    print("please wait for few seconds your request checking puropse ......")
    time.sleep(4)
    if checking_is_present[0][0] != None and checking_is_present1[0][0] != None:

        print("You have already debit card ")
    else:
        # print("Eles")
        def debit_card_number_generator():
            print(""" --------------------------------------
                      """)
            query = """SELECT DEBIT_CARD_NUMBER FROM USER_DETAILS Where DEBIT_CARD_NUMBER IS NOT NULL;"""
            already_debit_card_numbers_taken = read_query(connection, query)
            # print(already_debit_card_numbers_taken)# [(123456789009,), (123415778075,)]

            # print("already_debit_card_numbers_taken  : ", already_debit_card_numbers_taken)
            for i in range(len(already_debit_card_numbers_taken)):
                already_debit_card_numbers_taken[i] = already_debit_card_numbers_taken[i][0]
            # print(already_debit_card_numbers_taken)  # [123456789009, 123415778075]

            while True:
                deb_num = random.randint(100000000000, 1000000000000)
                if deb_num not in already_debit_card_numbers_taken:
                    break
            return deb_num

        deb_num = debit_card_number_generator()
        # print(deb_num)  # random number generating for debit card number --> 912967174920

        """update the debit card number into user_details table in bank database"""

        query_for_update_debit_card_number = f"""UPDATE USER_DETAILS SET DEBIT_CARD_NUMBER ={deb_num} WHERE ACCOUNT_NUMBER={ac};"""
        execute_query(connection, query_for_update_debit_card_number,
                          message="YOUR DEBIT CARD HAS BEEN SUCCESSFULLY APPLIED")

        """
                update the account_number,debit_card_number,date valid_from,date valid_upto)
                into DEBIT_CARD_DETAILS table in bank
            """

        # valid from (date) and valid up (date)
        def dating():
            current_date = date.today()

            # print(current_date)

            def add_year(current_date, year):
                try:
                    return current_date.replace(year=current_date.year + year)
                except ValueError:
                    return current_date.replace(year=current_date.year + year, day=28)

            current_date_plus_5year = add_year(current_date, 5)
            return current_date, current_date_plus_5year

        # print(current_date_plus_5year)
        valid_from, valid_up = dating()
        # print(valid_from, valid_up)
        query_inserting_values_debit_card_details = f"""
            INSERT INTO DEBIT_CARD_DETAILS (AC,DEBIT_CARD_NUMBER,VAILD_FROM,VAILD_UP)
            VALUES ({ac},{deb_num},STR_TO_DATE('{valid_from}','%Y-%m-%d'),STR_TO_DATE('{valid_up}','%Y-%m-%d'))
            """
        execute_query(connection, query_inserting_values_debit_card_details,
                          message="YOUR DEBIT CARD HAS BEEN SUCCESSFULLY CREATED")
        print("\n")
        deb_num="  ".join(str(deb_num))
        valid_f=f'{valid_from.month}/{valid_from.year}'
        valid_u=f'{valid_up.month}/{valid_up.year}'
        print(f"""
            --------------------------------------------
            |   CANARA BANK                  DEBIT CARD |
            |                                           |
            |   ------                                  |
            |   |    |                                  |
            |   ------                                  |
            |                                           |
            |  {deb_num}                  |
            |                                           |
            |   valid {valid_f}   valid {valid_u}           |
            |   from               upto                 |
            |                                           |
            |   CARD HOLDER NAME                        |
            ---------------------------------------------
            """)
        # pwd = maskpass.askpass(prompt="Password:", mask="*")
        # print(type(pwd))
        print("account : ",ac)

        # pin adding to database
        def seting_pin_number(pin):
            def encrypt_pin():
                # Generate a salt and hash the PIN
                salt = bcrypt.gensalt()
                hashed_pin = bcrypt.hashpw(pin.encode('utf-8'), salt)
                return hashed_pin
            hashed_pin=encrypt_pin()
            query_for_seting_pin=f"""UPDATE DEBIT_CARD_DETAILS SET PIN ="{hashed_pin}" WHERE AC={ac};"""
            execute_query(connection,query_for_seting_pin,message="YOUR DEBIT CARD HAS PIN NUMBER SUCCESSFULLY CREATED")
        while True:
            pwd=input("SET THE PIN NUMBER (4 number): ")
            if pwd.isdigit() and len(pwd)==4:
                break
            else:
                print("please enter proper number and digits  ")
        seting_pin_number(pwd)

def apply_credit_card(connection,ac):

    # to check already credit is or not

    #to checking in user_details table
    checking_credit_card_query = f"""SELECT CREDIT_CARD_NUMBER FROM USER_DETAILS Where ACCOUNT_NUMBER={ac};"""
    checking_is_present = read_query(connection, checking_credit_card_query)
    # print("checking_is_present : ", checking_is_present)

    #CREDIT_card_detail table checking
    checking_credit_card_query1 = f"""SELECT AC FROM CREDIT_CARD_DETAILS Where AC={ac};"""
    checking_is_present1 = read_query(connection, checking_credit_card_query1)
    # print("checking_is_present : ", checking_is_present1)

    print("please wait for few seconds your request checking puropse ......")
    time.sleep(4)
    # [(None,)]
    if checking_is_present[0][0] != None and checking_is_present1[0][0] != None:
        print("You have already credit card ")
    else:
        def credit_card_number_generator():
            print("""
        --------------------------------------
                      """)
            query = """SELECT CREDIT_CARD_NUMBER FROM USER_DETAILS Where CREDIT_CARD_NUMBER IS NOT NULL;"""
            already_credit_card_numbers_taken = read_query(connection, query)
            # print(already_credit_card_numbers_taken)# [(123456789009,), (123415778075,)]

            # print("already_credit_card_numbers_taken  : ", already_debit_card_numbers_taken)
            for i in range(len(already_credit_card_numbers_taken)):
                already_credit_card_numbers_taken[i] = already_credit_card_numbers_taken[i][0]
            # print(already_credit_card_numbers_taken)  # [123456789009, 123415778075]

            while True:
                cre_num = random.randint(100000000000, 1000000000000)
                if cre_num not in already_credit_card_numbers_taken:
                    break
            return cre_num

        cre_num = credit_card_number_generator()
        # print(cre_num)  # random number generating for credit card number --> 912967174920

        """update the credit card number into user_details table in bank database"""

        query_for_update_credit_card_number = f"""UPDATE USER_DETAILS SET CREDIT_CARD_NUMBER ={cre_num} WHERE ACCOUNT_NUMBER={ac};"""
        execute_query(connection, query_for_update_credit_card_number,
                          message="YOUR CREDIT CARD HAS BEEN SUCCESSFULLY APPLIED")

        """
                update the account_number,credit_card_number,date valid_from,date valid_upto)
                into DEBIT_CARD_DETAILS table in bank
        """

        # valid from (date) and valid up (date)
        def dating():
            current_date = date.today()

            # print(current_date)

            def add_year(current_date, year):
                try:
                    return current_date.replace(year=current_date.year + year)
                except ValueError:
                    return current_date.replace(year=current_date.year + year, day=28)

            current_date_plus_5year = add_year(current_date, 5)
            return current_date, current_date_plus_5year

        # print(current_date_plus_5year)
        valid_from, valid_up = dating()
        # print(valid_from, valid_up)
        query_inserting_values_credit_card_details = f"""
        INSERT INTO CREDIT_CARD_DETAILS (AC,CREDIT_CARD_NUMBER,VAILD_FROM,VAILD_UP)
        VALUES ({ac},{cre_num},STR_TO_DATE('{valid_from}','%Y-%m-%d'),STR_TO_DATE('{valid_up}','%Y-%m-%d'))
        """
        execute_query(connection, query_inserting_values_credit_card_details,
                          message="YOUR CREDIT CARD HAS BEEN SUCCESSFULLY CREATED")
        print("\n")
        cre_num="  ".join(str(cre_num))
        valid_f=f'{valid_from.month}/{valid_from.year}'
        valid_u=f'{valid_up.month}/{valid_up.year}'
        print(f"""
            --------------------------------------------
            |   CANARA BANK                  CREDIT CARD |
            |                                           |
            |   ------                                  |
            |   |    |                                  |
            |   ------                                  |
            |                                           |
            |  {cre_num}                  |
            |                                           |
            |   valid {valid_f}   valid {valid_u}           |
            |   from               upto                 |
            |                                           |
            |   CARD HOLDER NAME                        |
            ---------------------------------------------
            """)
        # pwd = maskpass.askpass(prompt="Password:", mask="*")
        # print(type(pwd))
        print("account : ",ac)

        # pin adding to database
        def seting_pin_number(pin):
            def encrypt_pin():
                # Generate a salt and hash the PIN
                salt = bcrypt.gensalt()
                hashed_pin = bcrypt.hashpw(pin.encode('utf-8'), salt)
                return hashed_pin
            hashed_pin=encrypt_pin()
            query_for_seting_pin=f"""UPDATE CREDIT_CARD_DETAILS SET PIN ="{hashed_pin}" WHERE AC={ac};"""
            execute_query(connection,query_for_seting_pin,message="YOUR CREDIT CARD HAS PIN NUMBER SUCCESSFULLY CREATED")
        while True:
            pwd=input("SET THE PIN NUMBER (4 number): ")
            if pwd.isdigit() and len(pwd)==4:
                break
            else:
                print("please enter proper number and digits  ")
        seting_pin_number(pwd)

