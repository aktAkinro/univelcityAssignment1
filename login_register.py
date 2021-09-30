

databaseName = []
databaseEmail = []
databasePass = []

print("Kindly Register Your account or sign Up")


registerName = input("Enter your Username?: ")
registerEmail = input("Enter your email?: ")
checker = databaseEmail.append(registerEmail)
print(databaseName)

special_characters = ["$", "#", "@","&", "*", "!", "%"]
isvalid = True
password = input("Enter a password: \n")
checker2 = databasePass.append(password)

if len(password) < 6:
    print("password should be at least 6")
    isvalid = False
    
elif len(password) > 16:
    print ("oops password too long. 16 characters at most")
    isvalid = False
elif not any(char.isdigit() for char in password):
    print("password should have at least one number")
    isvalid = False
elif not any(char.isupper()for char in password):
    print("password should have at least one uppercase letter ")
    isvalid = False
elif not any(char.islower() for char in password):
    print("password should have at least one lowercase letter")
    isvalid = False
elif not any (char in special_characters for char in password):
    print("password should have at least one symbol")
    isvalid = False
elif isvalid:
    print("password is valid")
else:
    print("password is invalid!")

    


    






print("You have now created an account?SignIn and get started: ")
loginEmail = input("Enter your Email?: ")




special_characters = ["$", "#", "@","&", "*", "!", "%"]
isvalid = True
password = input("Enter a password: \n")


if loginEmail in databaseEmail and password in databasePass:
    print("You are now logged in.")
else:
    print("password or username incorrect")





# the best way to start is by storng our data in a dictionary
# {email : password} and not a list.

# user_data = {}

# activity 