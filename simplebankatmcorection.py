import random
import time

user_data = {}
keep_running = True
logged_in = True


while keep_running:
    user_activity = input("Enter s to signup and any other key to login\n>>").lower()
    if user_activity=='s':
        name = input("Name:\n>>")
        pin = input("Enter 4 digit pin:\n>>")
        

            
        
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
                    print('Please take your cash')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
            elif action == '2':
                amount = float(input("Enter amount to deposit\n>>"))
                
                
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
                # elif action == '4':
                #         print(account_details)  
                else:
                    print('No active customer for this account number. Gerrout!')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break         
        else:
            print("Please enter a valid account number and pin")

                    