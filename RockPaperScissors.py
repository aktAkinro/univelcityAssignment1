# rock paper scissors 
# p w r
# s w p 
# r w s

import random
import time



RPS = ["Rock", "Paper", "Scissors"]

print("Welcome to \n Rock paper scissors")
username = input("please input your name?:")
print(f"Computer vs {username}")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")


choice = input(f"Pick your choice Rock, Paper, Scissors...{RPS}").title()
random.shuffle(RPS)
com_choice = random.choice(RPS).title()



print(com_choice)
print(choice)


if com_choice == choice:
    print("its a tie")
elif com_choice == RPS[0] and choice == RPS[1]:
    print("you win")
elif com_choice == RPS[0] and choice == RPS[2]:
    print("you lose")
elif com_choice == RPS[1] and choice == RPS[0]:
    print("you lose")
elif com_choice == RPS[1] and choice == RPS[2]:
    print("you win")
elif com_choice == RPS[2] and choice == RPS[0]:
    print("you win")
elif com_choice == RPS[2] and choice == RPS[1]:
    print("you lose")
else:
    print("incorrect input, please enter rock,paper, scissors")
    
