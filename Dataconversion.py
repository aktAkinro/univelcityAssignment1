# # first know the data type/structure of data before you can know what to convert and how to convert what to convert
student_data = {"name": "Jerry", "Courses":["Data Scien","Backend"], "scores" : {"Data Science": 20, "Backend": 15.7},}
# a = student_data["scores"]
# print(type(a))

# # str to int or float only if string is number
# int("100")

# # string to bool
# bool("True")


# whatever youre changing to stays outside the bracket

# only paired list in a tuple can convert to dictionary

# print(student_data.keys())
# print(type(student_data))

# print(list(student_data.keys()))

# list(student_data.keys())
print(type(list(student_data.keys())))


# dictionary to list would give just keys

print(list(student_data))