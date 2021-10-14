import random
import time
import ast

user_data = {}
transaction_record = {}
keep_running = True

print("Hello, Welcome to Bank App")
print(".")
time.sleep(0.5)
print(".")
time.sleep(2)

print("What would you like to do?")



while keep_running:
    user_activity = input("Enter\n\t S to signup,\n\t L to login \n\t and anyother key to quit\n>>").lower()

# input login details(name and password)
    if user_activity=='s':
        name = input("Name:\n>>").title()
        pin = input("Enter 4 digit pin:\n>>")

        # with open('BankInfo.txt', 'r') as bankinfo:
        #     banker = bankinfo.read()
        #     a = ast.literal_eval(banker)

# to randomly pick out 10 digits for account number. starting from 9.
#  the acc = "9" ensures that the first would always be 9 while you extend 9 digits to it       
        num = [str(i) for i in range(10)]
        acc = ['9']
        acc.extend([random.choice(num) for i in range(9)])
        account_num = "".join(acc)
        data = [('name', name), ('pin', pin), ('balance', 0)]
        user_data[account_num] = {}
        user_data[account_num].update(data)
        
        #create empty transaction record
        
        transaction_record[account_num] = []
        
        print(f"Hello {name}, your account has been successfully activated. Your account number is {account_num}.\n And your current balance is NGN0.\n\n\n Would you like to perform any transaction.")
        print(".")
        print(".")
        print(".")
        progress = input("Enter P to Proceed and any key to quit.\n>>").lower()
        if progress == 'p':
            continue
        else:
            break

#login
    elif user_activity=='l':
        print("Enter login details below".title())
        account_num = input("Account num:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        
        account_details = user_data.get(account_num, False)
        if account_details and account_details.get('pin')==pin:
            logged_in=True
            while logged_in:
                action = input(f"""Welcome, {account_details.get('name')}!
What would you like to do?
    1 for account statement
    2 for balance
    3 for deposit
    4 for transfer
    5 for withdrawal
Press any other key to logout\n>>""").lower()
                if action == '5':
                    amount = float(input("Enter amount to withdraw\n>>"))
                    
                    if amount >= account_details.get('balance', 0):
                        time.sleep(2)
                        print("Insufficiant funds")
                        
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                    else:
                        account_details['balance']-=amount
                        print('Please take your cash')
                        
                        #save transaction detail
                        
                        trans_data = {
                            'amount':amount,
                            'trans_type':'Debit',
                            'transaction':'Withdrawl'
                        }
                        
                        transaction_record[account_num].append(trans_data)
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                elif action == '3':
                    amount = float(input("Enter amount to deposit\n>>"))
                    
                    
                    account_details['balance']+=amount
                    print('Deposit complete')
                    
                    #save transaction detail
                        
                    trans_data = {
                        'amount':amount,
                        'trans_type':'Credit',
                        'transaction':'Deposit'
                    }
                    
                    transaction_record[account_num].append(trans_data)
                        
                    progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break   
                elif action == '4':
                    amount = float(input("Enter amount to transfer\n>>"))
                    recepient_account = input("Enter destination account number\n>>")
                    
                    recepient = user_data.get(recepient_account, False)
                    if recepient:
                        if amount >= account_details.get('balance', 0):
                            print("Insufficient funds.")
                        else:
                            account_details['balance']-=amount
                            #save transaction detail
                        
                            trans_data = {
                                'amount':amount,
                                'trans_type':'Debit',
                                'transaction':'Transfer'
                            }
                            
                            transaction_record[account_num].append(trans_data)
                        
                            recepient['balance']+=amount
                            
                            #save transaction detail
                        
                            beneficiary_trans_data = {
                                'amount':amount,
                                'trans_type':'Credit',
                                'transaction':'Transfer'
                            }
                            
                            transaction_record[recepient_account].append(beneficiary_trans_data)
                            
                            print("Transfer successful. Gerrout!")
                            progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                            if progress == 'p':
                                continue
                            else:
                                break
                    else:
                        print('No active customer for this account number. Gerrout!')
                        progress = input("Enter p to do something else and any key to logout.\n>>").lower()
                        if progress == 'p':
                            continue
                        else:
                            break
                elif action == '2':
                    print(f"Your current balance is NGN{account_details['balance']}\n")
                    
                elif action == '1':
                    
                    if len(transaction_record[account_num]) > 0:
                        last_5_transactions = transaction_record[account_num][-5:]
                        print("Here is your last 5 transactions")
                        for transaction in last_5_transactions:
                            print("Amount: ", transaction['amount'])
                            print("Transaction Type: ", transaction['trans_type'])
                            print("Transaction Ref.: ", transaction['transaction'])
                            print()
                    else:
                        print("You have not made any transactions. Please make a transaction.")
                        
                else:
                    break    
                
        else:
            print("Please enter a valid account number and pin")

    else:
        print("Thank you for banking with us. See you soon!")
        break


print(user_data)
print(transaction_record)





with open('BankInfo.txt', 'w') as bankinfo:
    bankinfo.write(f'{user_data}')

my_file = open("BankInfo.txt", mode = "a")
my_file.write(f"{trans_data}")

# with open('BankInfo.txt', 'r') as bankinfo:
#     banker = bankinfo.read()
#     a = ast.literal_eval(banker)


# my_file = open("BankInfo.txt", mode = "r")
# my_file.read()