
# special_characters = ["$", "#", "@","&", "*", "!", "%"]
# isvalid = True
# password = input("Enter a password: \n")

# if len(password) < 6:
#     print("password should be at least 6")
#     isvalid = False
# elif len(password) > 16:
#     print ("oops password too long. 16 characters at most")
#     isvalid = False
# elif not any(char.isdigit() for char in password):
#     print("password should have at least one number")
#     isvalid = False
# elif not any(char.isupper()for char in password):
#     print("password should have at least one uppercase letter ")
#     isvalid = False
# elif not any(char.islower() for char in password):
#     print("password should have at least one lowercase letter")
#     isvalid = False
# elif not any (char in special_characters for char in password):
#     print("password should have at least one symbol")
#     isvalid = False
# elif isvalid:
#     print("password is valid")
# else:
#     print("password is invalid!")




# print("Enter triangle sides: ")
# x=int(input("x: "))
# y=int(input("y: "))
# z=int(input("z: "))

# if x==y==z:
#    print("Equilateral triangle")
# elif x==y or y==z or z==x:
#    print("isosceles triangle")
# else:
#    print("Scalene triangle")




a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_list = sorted(a, key = lambda k:k["color"] )
print(sorted_list)







# num_qNewspaper = int(input(""))
# qNewspaper = input("")
# num_eNewspaper = int(input(""))
# eNewspaper = input("")

# f1 = set(qNewspaper.split())
# f2 = set(eNewspaper.split())

# final = f1.intersection(f2)
# print(len(final))





