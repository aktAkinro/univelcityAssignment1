# my_file = open("Tunde.txt", mode = "w")
# my_file.writelines(["This is e \n","This is second line"])
# my_file.write("This is write on write mode \nThis is second line")
# # be sure to run your code after this


# # in write mode if file doesmt exists it creates it
# # it gives ability to write to file 
# # a new one overwrites old one


# # .writelines gives a list of your lines and must be a list of strings




# # append mode 
# my_file = open("Tunde.txt", mode = "a")
# my_file.writelines(["This is e \n","This is second line"])
# my_file.write("This is write on write mode \nThis is second line")



# # append read ****
# my_file = open("BankInfo.txt", mode = "r")
# my_file.read()

import ast

d = {
    "name":"paul"
}
with open('des.txt', 'w') as paul:
    paul.write(f'{d}')
    
with open('des.txt', 'r') as mercy:
    favour = mercy.read()
    a = ast.literal_eval(favour)
    
# paul.write("I have risen")