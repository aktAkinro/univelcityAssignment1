import random
import time

bank_user = input("Please input your full name: \n")
user_pin = input("Input your 4 digit pin code: \n")
setup = True
default_balance = 00.00
user_acc_num = random.randrange(1334859696,1925637846)


for i in range(10000):
    if len(user_pin) == 4:
        print("valid pin")
        #   print(user_acc_num)
        time.sleep(2)
        print("..Just A Minute")
        time.sleep(2)
        print("..")
        print ("Hello {},\n\t Your autogenerated bank account number is  {}.".format(bank_user,user_acc_num))
        time.sleep(3)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print ("Hello {},\n\t You have successfully created your bank account with us. Your new account number is  {} and you have been automatically logged out for security reasons, kindly log in to get started.".format(bank_user,user_acc_num))
        time.sleep(2)
        print("..")
        time.sleep(3)
        print("..Welcome {}. Please Login".format(bank_user))
        time.sleep(2)
        login_acc = input("kindly input your account number: \n")
        login_pin = input("kindly input your pin: \n")
    else:
        print("Invalid Pin, Please start again and enter 4 digits")
        
    Bankactivity = input("kindly type W to withdraw, D to Deposite and T to transfer").lower()
    withraw = "w"
    deposit = "d"
    transfer = "t"
        
        

    if login_acc == user_acc_num or login_pin == user_pin:
        print("Login successful")
        time.sleep(2)
        print(".")
        time.sleep
        print("welcome {},\n\t You have successfully logged into your account and your account number is {}. Your account balance is N{}".format(bank_user,user_acc_num,default_balance))
    else:
        print("Incorrect Credentials")

        Bankactivity = input("kindly type W to withdraw, D to Deposite and T to transfer").lower()
        withraw = "w"
        deposit = "d"
    transfer = "t"

    while setup:
        if Bankactivity == deposit:
           deposit = int(input("How much would you like to Deposit?:\n"))
        if  deposit >= 0:
            print("Transaction Successful")
            new_balance = deposit + default_balance
            print("Hello {},\n\t You have successfully credited your account and Your account balance is N{}".format(bank_user,new_balance))
            break
        else:
            print("Invalid Transaction")
            
        if Bankactivity == withraw:
            how_much_to_withdraw = int(input("how much would you like to withdraw?: "))
            print(how_much_to_withdraw)
        
            if default_balance < int(how_much_to_withdraw):
                print ("insufficient funds") 
            else:
                print("Transaction Succesful")
                new_balance = default_balance - how_much_to_withdraw
                print("Hello {},\n\t Your Withdrawal Transaction is successful and Your account balance is N{}".format(bank_user,new_balance))
                break
        elif Bankactivity == transfer:
            how_much_to_transfer = int(input("how much would you like to Transfer?: "))
            print(how_much_to_transfer)
            if default_balance < how_much_to_transfer:
                print ("insufficient funds") 
            else:
                print("Transaction Succesful")
                new_balance = default_balance - how_much_to_transfer
                print("Hello {},\n\t Your Transfer Transaction is successful and Your account balance is N{}".format(bank_user,new_balance))
        else:
            input("kindly type W to withdraw, D to Deposite and T to transfer").lower()


    

    

    
     
     
