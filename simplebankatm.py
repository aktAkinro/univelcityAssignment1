input("Enter your Account Number")
print ("Current Account Balance: 25000")

strCHOICE = input ("Press 1 to make a Deposit or 2 to make a Withdrawal.")

if strCHOICE == 1:
    strDEPOSIT = input("Press 1 to deposit to checking, 2 for savings")
    if strDEPOSIT == 1:
      print("Please insert check or money now")
    elif strDEPOSIT == 2:
      print("Please insert check or money now")
 
elif strCHOICE == 2:
     strWITHDRAWAL = input("press 1 to draw funds from checking, press 2 for savings.")
     if strWITHDRAWAL == 1:
       input("How much would you like to withdraw today?")
       print("Please remove your cash from the slot below")
     elif strWITHDRAWAL == 2:
       input("How much would you like to withdraw today?")
       print("Please remove your cash from the slot below")

 


endofprogram = input("Thank you for your business, press enter to conclude this transaction.")