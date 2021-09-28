# a list is a collection of data that is ordered and changeable

# Lists are changeable(you can change certain characters) but they are ordered(They maintain their positio until end of code)
# a = [10,1,5,20,1,2,10,10]
# a[3] = 25

# print(a)


# # adding two strings together (joining) similar to concatination of strings
# first_list = [3,6,7]
# second_list = [8,8,10]
# full_list = first_list + second_list
# print(full_list)

# # list method
# # extend


# a = [1,2,3,4]
# b = [2,4,6,8]

# #a.append(12)
# a.extend(b)
# print(a)

# # create a list of usernames. then write a program to get input from user requesting for his first name and last name, generate a username for him. the user name should comprise of first 2 words
# #  of his last name and last two words of his first name. Add his username and print an output telling him his account has been created
# # hello, users first name 
# # thank you for signing up. 
# # your account has succcessfully been created. 
# # cheers, admin

# usernames = ["aktt", "btah", "fgst"]

# firstname = input("What is your firstname: ").title()
# lastname = input("What is your lastname: ")

# username = lastname[0] + lastname[1] + lastname[2] + firstname [-2] + firstname [-1]
# print(username)

# usernames.append(username)
# print (usernames)

# print ("Hello {},\n\t Thank you for signing up. Your account has successfully been created. Your account id is {} \n\t Cheers \n\t Admin".format(firstname,username))



# Given the list below [500,200,[200,500,700,[250,800]250],[1000]] 
# add 700 and 800 together and add the result to the list containing 1000 

# a = [500,200,[200,500,700,[250,800],250],[1000]]
# soln = a[2]
# soln700 = soln[2]
# print(soln700)

# solnn = (soln[3])
# soln800 = solnn[1]
# print(soln800)

# solution = soln700 + soln800

# a[3].append(solution)
# print(a)



# # find the last position of a substring "Emma" in a given string

# str1 = "Emma is a data scientist who knows python. Emma works at google"

# emmastring = str1.rindex('Emma')
# print(emmastring)

# a_list = [1, 2, "akt", 2]
# b_list = a_list.copy()
# c_list = a_list
# a_list[0] = 567
# print(a_list)
# print(b_list)
# print(c_list)


# remove - removes item with specified value

# a = [0,1,2,3,78]
# a.remove(78)
# print(a)


# pop - this removes the specified index and returns just the value. if the () is empty it removes last one

# ab = [1,34,34,78]
# ab_ = ab.pop(-1)
# print(ab_)

# insert - takes element and puts it into a specified position in a list. it takes in (index,value youwant to insert)

# list_ = [6,7,67,788,9864,1]
# print(list_)
# list_.insert(3,"hello people")
# print(list_)


# # sort and reverse

# # sort
# random_numbers = [1,445,565,67,876,88]
# random_numbers.sort()
# print(random_numbers)
# random_numbers.reverse()
# print(random_numbers)

# # it works with alphabets as well but not with words
# # pynative


# atuple = (1, 'John', 1+3j)
# print(type(atuple[2:3]))

# ase = ("i am a good".title()) 
# print(ase)

# l = [None] * 10
# print (len(l))

# a = [5,10,4]
# print(a[::-2])


# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.


# import time
# from decimal import Decimal



# list1 = [1,1,0,-1,-1]
# positive = []
# negative = []
# zero = []
# for i in list1:
#      if i > 0:
#          positive.append(i)
#      elif i < 0:
#          negative.append(i)
#      else: 
#          zero.append(i)


# ratio_p = (len(positive)) / len(list1)
# ratio_n = (len(negative)) / len(list1)
# ratio_z = (len(zero)) / len(list1)
# import decimal

# print(ratio_p)
# print(ratio_n)
# print(ratio_z)
# print('{:.6f}'.format(ratio_p))
# print('{:.6f}'.format(ratio_n))
# print('{:.6f}'.format(ratio_z))


# print(round(Decimal(ratio_p),6))

































