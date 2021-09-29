#  what is a module

# time module

import time
import random
from datetime import datetime



# print(time.time())
# # this returns the current time in seconds since january 1 1970

# print(time.gmtime())
# # this gives the particular time we are in 

# print(time.localtime())
# # this gives the local time we are in 

# print(time.sleep(3))
# # this stops time in python for a while. it adds a delay in python


# user = input("Enter: ")
# print("creating account, please wait..")
# time.sleep(3)
# print('.')
# time.sleep(3)
# print('.')
# time.sleep(3)
# print('.')
# time.sleep(3)
# print('.')

# print ()****


#  random allows you pick things randomly - for a dice game

# my_lift = [2,3,4,5,6,7]
# # random.shuffle(my_lift)
# # print(random.choice(my_lift))

# # # to randomly select 3 
# # print(random.sample(my_lift, 3))
# # print(my_lift)

# print(random.randrange(3,10))
# # this randomly picks a number within a range 

# random.seed(7)
# print(random.randrange(3,10))



# datetime

# to get curreent date and time
# print(datetime.now())
# print(datetime.now().second)
# print(datetime.now().minute)



#  strif time helps you convert the time to a string which is a more readable way.

# date = datetime.now()
# print(datetime.striftime(date,"%A, %d %B %Y"))
