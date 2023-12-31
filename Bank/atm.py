
# from bank import sql_connection
from sql import *
from existing_account import *
print("atm")
import bcrypt
connection=create_server_connection("localhost", "root", 'Dinesh1531@', 'bank')

def atm_functions(connection,ac):
    while True:
        l = ['Check_balance', 'Deposit_amount', 'Writhdraw_amount','exit']
        c = 1
        for i in l:
            print(f"{c}.{i}")
            c += 1
        c=0
        choose = input("Enter the choose option : ")

        if choose.isdigit():
            match int(choose):
                case 1:
                    check_balance(connection, ac)
                case 2:
                    deposit(connection, ac)
                case 3:
                    writhdraw(connection, ac)
                case 4:
                    break
                case _:
                    print("Please enter valid option")
        else:
            print("please enter the digit !")
        continue1 = input("DO YOU WANT TO CONTINUE (YES/NO)")
        if continue1[0].lower() == 'n':
            break


while True:
    try:
        card_type = input("Enter the card type (debit ->1 /credit ->2) : ")
        if card_type.isdigit():
            option=int(card_type)
            if option==1:
                card_type='DEBIT'
            elif option==2:
                card_type='CREDIT'
            else:
                print("please enter valid card type!")
                break
        else:
            print("Please enter valid card type !")
            break
    except Error as er:
        print("Error : ",er)



    try:

        debit_credit = int(input(f"Enter the {card_type} number : "))

        pswd=input("Enter the pin : ")
        query_account_numbers = f"""select PIN  FROM {card_type}_card_details Where {card_type}_CARD_NUMBER={debit_credit};"""
        PIN_hased_password = read_query(connection, query_account_numbers)
        hashed_password=PIN_hased_password[0][0]
        print(hashed_password)
        if bcrypt.checkpw(pswd.encode('utf-8'), hashed_password):
            print("Password is correct!")
        else:
            print("Password is incorrect.")
        res = []
        query_account_numbers = f"""select ACCOUNT_NUMBER FROM USER_DETAILS Where {card_type}_CARD_NUMBER={debit_credit};"""
        account_numbers = read_query(connection, query_account_numbers)
        for i in account_numbers:
            res.append(i[0])
        if res:
            atm_functions(connection,res[0])
            res.clear()
            break
        else:
            print("enter the vaild account number !")

    except ValueError:
        print("Please enter the valid account number (not in integer)  ")






