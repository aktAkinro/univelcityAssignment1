# # a dictionary is with key value pairs sep by colon. you can change values and key

# my_diction = {"color":"Brown", "pet":"Dog", "Name": "Funmi", "Course": "Anatomy"} 
# # to change

# my_diction["color"] = "Yellow"
# print(my_diction)


# # to get use key

# my_diction["pet"]
# # in this method if key doesnt exist it gives key error
# print(my_diction.get("pet"))
# # in this method it would give none if key is abscent.
# #  this is preferably if you use a key that doesnt exist but you want to put something else to replace. 
# # for example if key value is not there put nigeria

# print(my_diction.get("country"))
# # this above would give none because it isnt part of your above keys in my_diction
# print(my_diction.get("country","Nigeria"))

# # the above would replace none with nigeria





# # to create a new key
# my_diction["country"] = "Naija"
# print(my_diction)
# dic[k] = val 



#  to find out all the keys available 

#   get an input from the user ask for his course and score. add his course to courses and his score to score

# student_data = {"name": "Jerry", "Courses":["Data Scien","Backend"], "scores" : {"Data Science": 20, "Backend": 15.7},}

# courseName = input("what course are you studying?: ")
# score = input("what score did you get?: ")

# student_data["Courses"].append(courseName)
# student_data["scores"][courseName] = score


# print(student_data)


# my_dict.keys will give all keys, my_dict.values give aall values and my_dct.value give a tuple of all values
# print(student_data.keys())


# my_dictionary = {
#     "name": "Tunde",
#     "gender": "Male",
# }

# my_dictionary.update({'key': 'value'})
# list_of_tuples = [("john","Abuja"), ("Nigeria","Naija")]
# # like the above you can update using tuples

# my_dictionary.update(list_of_tuples)
# print(my_dictionary)



# pop method you pop the key and it gives you the value
# b = student_data.pop("name")
# print(b)



# how can we change key called score in student data to change to result

# pop scores out first

# var = student_data.pop("scores")
# print(var)
# print(student_data)
# student_data["result"] = var 
# print(student_data)

# print(type(student_data))








#### QUESTIONS





# change Brads salary to 8500

# sampleDict = {
#     "emp1" : {'name' : "Jhon", 'salary': 7500},
#     "emp2" : {'name' : "Emma", 'salary': 8000},
#     "emp3" : {'name' : "Brad", 'salary': 6500},

# }

# sampleDict ["emp3"]["salary"] = 8500
# print(sampleDict)


# writea program that takes in the user details and saves it in the user dictionary following format below 
# 
# users = {usern : {"first_name" : "firstname", "last_name" : "lastname"}
#     }


# user = {}

# firstN = input("what is your first name?: ")
# lastN = input("what is your last name?: ")
# username = firstN[:3] + lastN[-3:]

# user[username] = {}
# user [username]["first_name"] = firstN
# user [username]["last_name"] = lastN
# print(user)



# Given the list below: [2,2,4,6,7,2,4,4,3,6,2,1]
#  write a program to remove duplicates from list and sort it. Expected output is [1,2,3,4,6,7]
    
# typelist = [2,2,4,6,7,2,4,4,3,6,2,1]
# type2list = set(typelist)
# type3list = list(type2list)

# print(type3list)


# # write a program to convert a list of multiple integers to a single integer. ["11","55","33"]

# a = ["11","55","33"]
# b = "".join(a)
# c = int(b)
# print(c)

 

# #   write a program to unpack a tuple into several variables

# atuple = ("a",12,34.5,"game")
# a,b,c,d = atuple

# print(a)
# print(b)
# print(c)
# print(d)

# # write a program to convert a tuple below to a string.

# univel = ("u","n","i","v","e","l","c","i","t","y")

# univel1 = list(univel)
# univel2 = "".join(univel1)
# print(univel2)







