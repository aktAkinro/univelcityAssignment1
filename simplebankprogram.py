import random
import time

user_data = {}
keep_running = True
logged_in = True
transaction_log = {}



while keep_running:
    user_activity = input("Enter s to signup and any other key to login\n>>").lower()
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")

        if pin.isdigit() and len(pin) == 4:
            print("You successfully logged in!")
        else:
            print("Only 4 digits allowed")
            break
        

            
        
        num = [str(i) for i in range(10)]
        acc = ['9']
        acc.extend([random.choice(num) for i in range(9)])
        account_num = "".join(acc)
        data = [('name', name), ('pin', pin), ('balance', 0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        # print(user_data)
        print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.")
        time.sleep(2)
        print(".")
        print(".")
        print(".")
        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break
    else:
        print("Enter login details below".title())
        account_num = input("Account num:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
    while logged_in:
        account_details = user_data.get(account_num, False)
        if account_details and account_details.get('pin')==pin:
            action = input(f"""Welcome, {account_details.get('name')}!
What would you like to do?
    1 for withdrawal
    2 for deposit
    3 for transfer
    4 To check Balance
    5 To get bank statement
Press any other key to quit\n>>""").lower()
            if action == '1':
                amount = float(input("Enter amount to withdraw\n>>"))
                # transaction_log[account_num]["balance"] -= amount
                # data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                # transaction_log[account_num].append(data_)
                
                if amount >= account_details.get('balance', 0):
                    time.sleep(2)
                    print("Insufficiant funds")
                    print("Session Expired")
                    
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
                else:
                    account_details['balance']-=amount
                    transaction_log[account_num] = []
                    # data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                    # transaction_log[account_num].append(data_)
                    print('Please take your cash')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
            elif action == '2':
                amount = float(input("Enter amount to deposit\n>>"))
                # transaction_log[account_num]["balance"] += amount
                # data_ = [{"amount": amount},{"alert type":"credit"},{"transaction type":"deposit"}]
                # transaction_log[account_num].append(data)
                
                account_details['balance']+=amount
                print('Deposit complete')
                progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                if progress == 'p':
                    continue
                else:
                    break   
            elif action == '3':
                amount = float(input("Enter amount to transfer\n>>"))
                recepient_account = input("Enter destination account number\n>>")
                # transaction_log[account_num]["balance"] -= amount
                # data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                # transaction_log[account_num].append(data_)
                
                recepient = user_data.get(recepient_account, False)
                if recepient:
                    if amount >= account_details.get('balance', 0):
                        print("Insufficient funds. GERROUT!")
                    else:
                        account_details['balance']-=amount
                        recepient['balance']+=amount
                        print("Transfer successful. Gerrout!")
                        progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
            elif action == '4':
                    print("Getting your account balance....")
                    time.sleep(1)
                    print(f"Your Account Balance is NGN{user_data[account_num]['balance']}\n")
                    if progress == 'p':
                        continue
                    else:
                        break
            elif action == '5':
                    print("hi")
                    if progress == 'p':
                        continue
                    else:
                        break

            else:
                print('incorrect input')
                progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                if progress == 'p':
                    continue
                else:
                    break         
    else:
        print("Please enter a valid account number and pin")





# import random
# import time

# bank_user = input("Please input your full name: \n")
# user_pin = input("Input your 4 digit pin code: \n")
# setup = True
# default_balance = 00.00
# user_acc_num = random.randrange(1334859696,1925637846)


# # for i in range(10000):
# if len(user_pin) == 4:
#       print("valid pin")
#     #   print(user_acc_num)
#       time.sleep(2)
#       print("..Just A Minute")
#       time.sleep(2)
#       print("..")
#       print ("Hello {},\n\t Your autogenerated bank account number is  {}.".format(bank_user,user_acc_num))
#       time.sleep(3)
#       print(".")
#       time.sleep(2)
#       print(".")
#       time.sleep(1)
#       print ("Hello {},\n\t You have successfully created your bank account with us. Your new account number is  {} and you have been automatically logged out for security reasons, kindly log in to get started.".format(bank_user,user_acc_num))
#       time.sleep(2)
#       print("..")
#       time.sleep(3)
#       print("..Welcome {}. Please Login".format(bank_user))
#       time.sleep(2)
#       login_acc = input("kindly input your account number: \n")
#       login_pin = input("kindly input your pin: \n")
# else:
#       print("Invalid Pin, Please start again and enter 4 digits")
     
      

# if login_acc == user_acc_num or login_pin == user_pin:
#       print("Login successful")
#       time.sleep(2)
#       print(".")
#       time.sleep
#       print("welcome {},\n\t You have successfully logged into your account and your account number is {}. Your account balance is N{}".format(bank_user,user_acc_num,default_balance))
# else:
#       print("Incorrect Credentials")

# Bankactivity = input("kindly type W to withdraw, D to Deposite and T to transfer").lower()
# withraw = "w"
# deposit = "d"
# transfer = "t"

# while setup:
#     if Bankactivity == deposit:
#       Deposit = int(input("How much would you like to Deposit?:\n"))
#       if  Deposit >= 0:
#         print("Transaction Successful")
#         new_balance = Deposit + default_balance
#         print("Hello {},\n\t You have successfully credited your account and Your account balance is N{}".format(bank_user,new_balance))
#         break
#       else:
#         print("Invalid Transaction")
#         break
#     elif Bankactivity == withraw:
#       how_much_to_withdraw = int(input("how much would you like to withdraw?: "))
#       print(how_much_to_withdraw)
    
#       if default_balance < int(how_much_to_withdraw):
#           print ("insufficient funds") 
#       else:
#         print("Transaction Succesful")
#         new_balance = default_balance - how_much_to_withdraw
#         print("Hello {},\n\t Your Withdrawal Transaction is successful and Your account balance is N{}".format(bank_user,new_balance))
#         break
#     elif Bankactivity == transfer:
#      how_much_to_transfer = int(input("how much would you like to Transfer?: "))
#      print(how_much_to_transfer)
#      if default_balance < how_much_to_transfer:
#           print ("insufficient funds") 
#      else:
#         print("Transaction Succesful")
#         new_balance = default_balance - how_much_to_transfer
#         print("Hello {},\n\t Your Transfer Transaction is successful and Your account balance is N{}".format(bank_user,new_balance))
#     else:
#         input("kindly type W to withdraw, D to Deposite and T to transfer").lower()


    

    

    
     
     
