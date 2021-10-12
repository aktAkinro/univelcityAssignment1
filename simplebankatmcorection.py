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
        credit = []
        debit = []
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
                user_data[account_num]["balance"] -= amount
                data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                transaction_log[account_num].append(data_)
                print(f"***Debit Alert*** ***Withdrawal*** ***Amount: {amount}***")
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
                    user_data[account_num] = []
                    data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                    transaction_log[account_num].append(data_)
                    print('Please take your cash')
                    progress = input("Enter p to do something else and any key to quit.\n>>").lower()
                    if progress == 'p':
                        continue
                    else:
                        break
            elif action == '2':
                amount = float(input("Enter amount to deposit\n>>"))
                transaction_log[account_num]["balance"] += amount
                data_ = [{"amount": amount},{"alert type":"credit"},{"transaction type":"deposit"}]
                transaction_log[account_num].append(data)
                
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
                print(f"***Debit Alert*** ***Transfer*** ***Amount: {amount}***")
                recepient = user_data.get(recepient_account, False)
                if recepient:
                    if amount >= account_details.get('balance', 0):
                        print("Insufficient funds. GERROUT!")
                    else:
                        account_details['balance']-=amount
                        recepient['balance']+=amount
                        print("Transfer successful. Gerrout!")
                        # transaction_log = {}
                        # transaction_log[account_num]["balance"] -= amount
                        # data_ = [{"amount": amount},{"alert type":"debit"},{"transaction type":"withdraw"}]
                        # transaction_log[account_num].append(data_)
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

                    