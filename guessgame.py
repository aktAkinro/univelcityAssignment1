import random


print("welcome to my guess name")
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
choice = int(input(f"Guess number from: \n {list_of_numbers}\n>>"))

# list_of_numbers.remove(choice)
#  this is to remove any choice the user picks and so they can never win
random.shuffle(list_of_numbers)

com_choice = random.choice(list_of_numbers)

if choice == com_choice:
    print("you win")
else: 
    print("E be like say you no win o ")





