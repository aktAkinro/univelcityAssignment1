# functions built into python and used regularly by programmers

# input enables interactivity between user and python code. you can enter a prompt

# len() it returns the length of any interable like tuples,sets, etc

# sum() adds up all items in an iterable usually numbers and returns total


# lambda is a way of writing our own function but it isnt a fully fledged function.
#  its like facebook lite to facebook. it can only have one expression. 
# lambda variable.title(variable) 

# map executes a specified function for each item in an iterable.
#  it takes in (function,iterable)

# li = [1,2,3,4,5]
# lambda i : i**2

# l2 = list(map(lambda i : i**2,li))
# print(l2)




# # QUESTION - Write a program that takes in input from user asking him for a lis of the 
# # prices of items bought in x days separated by comma
# items_bought = input("cost of every item bought?:\n").split(',')
# numbers = list(map(lambda string: int(string), items_bought))
# print(sum(numbers))
# print(sum(numbers)/len(numbers))




# min() to get minimum value AND max for maximum

# zip() takes two iterables and pairs them together as a tuple. 
# if you convert to list it becomes list of tuples.
#  if both lists have unequal number of elements it throws away the last

# customers = ["femi","tunde","ayo","frank"]
# price = [2000,4000,5000,6000,000]
# d = dict(zip(customers,price))
# li = list(zip(customers,price))
# o = tuple(zip(customers,price))
# s = set(zip(customers,price))
# print(d)
# print(li)
# print(o)
# print(s)



#  enumerate zips the value with the index(or counter). you must convert it to list before printing

# customers = ["femi","tunde","ayo","frank"]
# f = enumerate(customers)
# print(list(f))


# filter is like map 

# here get the even numbers from the list below.
# to get even numbers use a % 2 and if it gives 0 then it means it is even
# mylist = [2,3,4,5,6,7,8,99,9,60]
# o = list(filter(lambda a:a % 2 == 0, mylist))
# print(o)

# range gives range object so must be converted to list or something else
# myrange = [1,2,3,4,5,6]
# m = range(2,5,2)
# print(list(m))
