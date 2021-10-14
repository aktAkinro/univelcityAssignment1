from os import name
import time
keep_running = True
user_data = {}
loop = True
logged_In = True


        



while keep_running:
    user_activity = input("Enter\n\t S to signup,\n\t L to login \n\t and anyother key to quit\n>>").lower()

    if user_activity=='s':
        ("Welcome to kidsco Diaries, Kindly fill in the following to get started")
        time.sleep(1)
        print(".")
        print(".")
        Firstname = input("First Name? :\n>>").title()
        Lastname = input("Last Name? :\n>>").title()
        username = input("what is your username\n")
        Email_Address = input("Enter your Email? :\n>>").title()
        password = input("Enter your password:\n>>")
        confirmation = input("Confirm your password:\n>>")
        print(f"Hello {Firstname}")
        # my dictionary, key is Firstname
        data = [("name", Firstname),("Lastname", Lastname),("password",password),("Email",Email_Address)]
        user_data[username]= {}
        user_data[username].update(data)
        print(user_data)

        if password != confirmation:
            print("incorrect password pair, try again")
            password = input("Enter your password:\n>>")
            confirmation = input("Confirm your password:\n>>")
        else:
            continue
    elif user_activity=='l':
        firstname = input("Input Username:\n>>").lower()
        Password = input("Enter Password:\n>>")

        name = user_data.get(firstname, False)


        while (loop == 'true'):
            print("Enter login details below".title())
            if (Firstname == firstname) and (Password == password):
                print("Login Successful")
                time.sleep(2)
                print(".")
                print(".")
            else:
                print ("incorrect credentials!")
        while logged_In:
                action = input(f"""Welcome, {Firstname}!
What would you like to do?
    1 View Profile
    2 Create note
    3 Edit Note
    4 Edit Profile
    5 Change password
Press any other key to logout\n>>""").lower()
                if action == "1":
                    print(user_data)
                    print(f"\n\tFirst Name: {Firstname}\n\t Last Name: {Lastname}\n\t Email: {Email_Address}")
                elif action == "2":
                    file = username
                    with open(f" {username}.txt ", "w") as doc:
                        doc.write(input("write something here:..."))

                 
                elif action == "4":
                    print(f"\n\tFirst Name: {Firstname}\n\t Last Name: {Lastname}\n\t Email: {Email_Address}")
                    Edit = input(f"""Hello, {Firstname}!
Which would you like to Edit?
    F First Name
    L Last Name
    E Email
    P Change Password
Press any other key to go back\n>>""").upper()
                    if Edit == "F":
                        new_first = input("Input First Name?: ")
                        user_data[username]['name'] = new_first
                    elif Edit == "L":
                        new_last = input("Input Last Name?: ")
                        user_data[username]['Lastname'] = new_last
                    elif Edit == "E":
                        new_Email = input("Input Email?: ")
                        user_data[username]['Email'] = new_Email
                    elif Edit == "P":
                        current_pass = input("What is your current password?: ")
                        if current_pass == password:
                            new_pass = input("what is your new password?: ")
                            user_data[username]['password'] = new_pass
                    else:
                        continue
                    print(user_data)
                elif action == "5":
                    current_pass = input("What is your current password?: ")
                    if current_pass == password:
                        new_pass = input("what is your new password?: ")
                        user_data[username]['password'] = new_pass
                        print(user_data)
                        
                    else: 
                        print("incorrect PInput, Enter correct password")

                else:
                    print("Goodbye {firstname}")
                    break
    else:
        print("Goodbye, see you next time")
        break






    # a loop is needed for password confirmation