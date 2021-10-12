# DRY - DONT REPEAT YOURSELF

# FUNCTIONS ARE USUALLY USED IN DRY CASES

# How to define

# def func_name():
#     block of code

# a function is useless unless called. you can call like
# functionname()


# def generate_pass():
#     print("something")

# generate_pass() # something only prints when function is called


# # a parameter is whatever passed in () when defining function
# # an argument is whatever is passed in () when calling function

# def add_num(x,y): # this x and y serve as parameter
#     a = x+y
# # add_num(2,4)    # this 2 and 4 serve as argument

# def add_num2(x,y): 
#     a = x+y
#     return(x+y)
    
# # add_num(2,4)    
# a = add_num(2,4)
# b = add_num2(2,4)

# print(a) # this would give none
# print(b)

# return statementis used to return output of the function just like "print"
# print only gives output but return doesnt only print it it gives ability to add it to a variable
# pop is an example, it has return statement

#  anything after the return statement wont work. it would grey out

# the number of arguments passed must equal number of parameters defined


# an arbituary function is used when we dont know the number of arguments to bee used
# it can take as many arguments

# def func_names (*names):
#     print("hello" + names[1])
# func_names("james","ak","asd")




# write function to calc 

# - mean
# - median
# - mode 
# - standard dev
# - variance
# - find prime numbers

numbers = [1,2,3,4,5,4]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# def mean (numbers):
#      return (sum(numbers)/len(numbers))

# print(mean(numbers))




# def median (sorted_numbers):
    
#     index = len(sorted_numbers)//2
#     print(index)

#     if len(sorted_numbers) % 2 != 0:
#         return sorted_numbers[index]
#     else:
#         return(sorted_numbers[index-1] + sorted_numbers[index])/2
# print(median(numbers))
    
    


    

# def variance (numbers):
#     var = (numbers - mean)/len(numbers)
#     return(numbers)