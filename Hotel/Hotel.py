# ---------------------------- DISPLAY ---------------------------------------------------------
def welcome():
    print("\t\tWELCOME TO ELITE HOTEL")
    print("\t\t**********************")
    print("\t\t1.Indian Food Items")
    print("\t\t2.Italian Food Items")
    print("\t\t3.Chinese Food Items")

indian_food_items_veg={1:['Pongal',50], 2:['Masala dosa',75],3:['Onion Roast',70],4:['Poori',30],5:['Tomato Rice',50],6:['Lemon Rice',40]}
indian_food_items_N_veg = {7:['Chicken Chettinad',250],8:['Thalassery Biriyani',300],9:['Pandi Curry',214],10:['Chicken 65',150]}
indian={}
indian.update(indian_food_items_veg)
indian.update(indian_food_items_N_veg)

italian={1:['Pizza',250],2:['Pasta',200],3:['Arancini',140],4:['Focaccia',100],5:['Lasagna',240],6:['Truffles',570],7:['Ossobuco',450]}
chinese={1:['Kung Pao Chicken',79],2:['Sweet and Sour Pork',120],3:['Peking Roast Duck',450],4:['Mapo Tofu',310],5:['Chow Mein',340],6:['Spring Rolls',250],7:['Chicken Fried Rice',100]}
total={}


# ----------------------------------------  WORKING ------------------------------------------------------------
def Indian_foods():
    n = 1

    while n != 0:
        if n != 0:
            print("-------------------------\nIndian Veg Food items\n")
            for i in indian_food_items_veg:
                print(i, indian_food_items_veg[i][0])

            print("-------------------------\nIndian Non-Veg Food items\n")
            for i in indian_food_items_N_veg:
                print(i, indian_food_items_N_veg[i][0])
            choice = input("enter the indian any one food : ")


            if choice.isdigit() and int(choice) in indian.keys():
                choice=int(choice)
                # print(indian.keys())
                count = input(f"How Many count  {indian[choice][0]} ?")
                if count.isdigit():
                    count=int(count)
                    if indian[choice][0] not in total:
                        # print(total)
                        total[indian[choice][0]] = [count, indian[choice][1], indian[choice][1] * count]
                        # print(total)
                    else:
                        update_count = total[indian[choice][0]][0] + count
                        old_amount = total[indian[choice][0]][2]
                        update_amount = old_amount + (indian[choice][1] * count)
                        total[indian[choice][0]] = [update_count, indian[choice][1], update_amount]
                        # print("new total : ", total)
                else:
                    print("please enter valid count --")
                def indian_food_continue(n):
                    rs = 1
                    while rs != 0:
                        restart = True
                        if restart == True:
                            def indian_continue_correct(con):
                                if con[0].lower() == 'y':
                                    pass
                                elif con[0].lower() == 'n':
                                    return 0

                            con = input("Do you want to you continue to order indian food (Y/N) : ").lower()
                            if con in ['y', 'n']:
                                n = indian_continue_correct(con)
                                restart = False
                                return n
                            else:
                                print("please enter valid information")

                n = indian_food_continue(n)
                if n == 0:
                    break

            else:
                print("Please enter valid information")

        else:
            # print("break")
            break

# --------------------------------   ITALIAN FOOD -----------------------------------------------
def Italian_foods():
    n = 1

    while n != 0:
        if n != 0:
            print("-------------------------\nItalianFood items\n")
            for i in italian:
                print(i, italian[i][0])


            choice = input("enter the italian any one food : ")


            if choice.isdigit() and int(choice) in italian.keys():
                choice=int(choice)
                # print(italian.keys())
                count = input(f"How Many count  {italian[choice][0]} ?")
                if count.isdigit():
                    count=int(count)

                    if italian[choice][0] not in total:
                        # print(total)
                        total[italian[choice][0]] = [count, italian[choice][1], italian[choice][1] * count]
                        # print(total)
                    else:
                        update_count = total[italian[choice][0]][0] + count
                        old_amount = total[italian[choice][0]][2]
                        update_amount = old_amount + (italian[choice][1] * count)
                        total[italian[choice][0]] = [update_count, italian[choice][1], update_amount]
                        print("new total : ", total)
                else:
                    print("Please enter the valid information ---")

                def italian_food_continue(n):
                    rs = 1
                    while rs != 0:
                        restart = True
                        if restart == True:
                            def italian_continue_correct(con):
                                if con.lower() == 'y':
                                    pass
                                elif con.lower() == 'n':
                                    return 0

                            con = input("Do you want to you continue to order italian food (Y/N) : ").lower()
                            if con in ['y', 'n']:
                                n = italian_continue_correct(con)
                                restart = False
                                return n
                            else:
                                print("please enter valid information")


                n = italian_food_continue(n)
                if n == 0:
                    break

            else:
                print("Please enter valid information")

        else:
            print("break")
            break
#--------------------  ---------------------   CHINESE FOOD -------------------------------
def Chinese_foods():
    n = 1

    while n != 0:
        if n != 0:
            print("-------------------------\nChinese Food items\n")
            for i in chinese:
                print(i,chinese[i][0])


            choice = input("enter the chinese any one food : ")


            if choice.isdigit() and int(choice) in chinese.keys():
                choice=int(choice)
                # print(chinese.keys())
                count = input(f"How Many count  {chinese[choice][0]} ?")
                if count.isdigit():
                    count=int(count)

                    if chinese[choice][0] not in total:
                        # print(total)
                        total[chinese[choice][0]] = [count, chinese[choice][1], chinese[choice][1] * count]
                        # print(total)
                    else:
                        update_count = total[chinese[choice][0]][0] + count
                        old_amount = total[chinese[choice][0]][2]
                        update_amount = old_amount + (chinese[choice][1] * count)
                        total[chinese[choice][0]] = [update_count, chinese[choice][1], update_amount]
                        # print("new total : ", total)
                else:
                    print("Please enter the valid information ---")

                def chinese_food_continue(n):
                    rs = 1
                    while rs != 0:
                        restart = True
                        if restart == True:
                            def chinese_continue_correct(con):
                                if con.lower() == 'y':
                                    pass
                                elif con.lower() == 'n':
                                    return 0

                            con = input("Do you want to you continue to order chinese food (Y/N) : ").lower()
                            if con in ['y', 'n']:
                                n = chinese_continue_correct(con)
                                restart = False
                                return n
                            else:
                                print("please enter valid information")

                n = chinese_food_continue(n)
                if n == 0:
                    break

            else:
                print("Please enter valid information")

        else:
            print("break")
            break


#-----------------   ------------------  BILLING DEPARTMENT -----------------
def billing_counter():
    print('-------------------------------------------------------------------------------')
    li=['S.No','Food name','Quantity','Price(peritem)','Quan*Price']
    print(f' {li[0]:<5}| {li[1]:<26}| {li[2]:<10}| {li[3]:<18}| {li[4]:<10} |')
    print('-------------------------------------------------------------------------------')
    sno=1
    total_amount=0
    for i in total:
        print(f'| {sno:<4}| {i:<26}| {total[i][0]:<10}| {total[i][1]:<18}| {total[i][2]:<10} |')
        sno+=1
        total_amount+=total[i][2]
    if len(total)!=0:
        print('-------------------------------------------------------------------------------')
        print(f'|\t\t\t\t\t\t\t\t\t\t\t\t\t Total amount to pay : {total_amount}|')
        print('-------------------------------------------------------------------------------')

n=1
while n!=0:
    welcome()
    while True:
        try:
            n=int(input("0 Exit  \nSelect the which origin food Style : "))
            break
        except ValueError:
            print("Please enter the valid option ! ")
    match n:
        case 1:


            Indian_foods()
        case 2:

            Italian_foods()

        case 3:
            Chinese_foods()

        case 0:
            if len(total)!=0:
                billing_counter()
            else:
                print("You can't ordered any food . How can generate the bill?")
        case _:
            print("Please valid food items")

