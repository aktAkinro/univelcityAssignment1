# # # concatenation using +


# print("Beautiful" + "city")
# print("Beautiful" + " city")

# # # index - the first letter starts with 0 then 1 and 2 and then the numbering continues.
# # # Akinro
# # # 012345



# name = "akinro"
# print(name[3])

# # # ngative indexing is from back to front opposite of positive or normal indexing. this can be used if you want to get the last element in a string and you dont know how long it is


# # print(name[-3])


# # # string slicing [start:end] rem your first index is 0


# # #  Given two strings first name and last name, write a program to
# # # - Concatenate the two strings remember to add space and assign to variable full name
# # # - slice out last name from full name


# firstName = "Akintunde"
# lastName = "Akinro"

# print("Akintunde" + " Akinro")
# #      012345678     9


# fullName = (firstName + lastName)

# print(fullName[0:9])
# print(fullName[-6:])

# # # when there is no value at the first [.:4] then it is everything from beginning to that point

# # # when we have [2:8:2] it means move from index 2 to 8 in steps of 2

# # new_string = "blue sky"
# # print(new_string[2:8:2])
# # print(new_string[2:5])
# # print(new_string[:5])
# # print(new_string[2:])


# # # stringformatting is used when you dont want to hardcode data that is you dont want the data to be assigned to a particular name or price for example when giving out an invoice.
# # # you must include f at the begining and also include the variable in {}
# # namae = "Akintunde"
# # price = 20
# # print(f"welcome {name}. You are to pay NGN {price}")

# # or , for one variable

# myname = "Joy"
# myprice = 200
# print("welcome {}. You have just signed in".format(myname))
# print("welcome {}. You are to pay {}".format(myname,myprice))


# ## for many variables introduce the function input and what ever value you input would be passed as a string

# # username = input("Tell us who you are: ")


# # print("welcome {}. You have just signed in".format(username))



# # QUESTON - write a program that takes in your name and age of a user then tells him what year he was born

# yourname = input ("what is your name: ")
# yourage = input ("How old are you: ") 
# yob = (2021-int(yourage))


# print(2021-int(yourage))


# # print(type(yourage))


# # print(type(int(yourage)))

# # print ("welcome {},\n\t you are {} years old \n\t you were born in {}".format(yourname,yourage,yob))




# # escape characters 
# # \ helps with;
# # print('Her father\'s daughter')
# # \n helps shft text to next line
# # \t helps give tab or space

# # print ("welcome {},\n\t you are {} years old".format(yourname,yourage))




# # string methods
# #title turns first letter of all words to capital

# # name = input('who are you')
# # print(name.title())

# # name2 = input('who  you').title()
# # print(name2)


# # upper() converts the whole string to uppercase, lower is opposite

# # name = "Jack".startswith("J")
# # print(name)

# # name = "Jack".endswith("J")
# # print(name)

# # justreg = "JACK".lower()
# # print(justreg)

# # title = "jack".title()
# # print(title)



# #index vs find they both look for the position of a value but find gives -1 if it doesnt find it while index gives error

# # print(justreg.find('a'))
# # print(justreg.index('a'))

# # if we find J we wont see it since we have j in small letters


# # isspace returns true if it has space
# # isnumeric if it has numbers
# # isalphanumeric if it contains alphabets and numbers
# #islower if it contains all lower case


# # # split and join. 
# # # split
# myfullname = "akinro akintunde akolawole"
# name_list = myfullname.split()
# # split turns it to a list and each item in the list has an index starting from zero [0,1,2] [akinro, akintunde, akolawole]
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])

# #join
# mynamelist = ['akinro', 'akintunde' , 'akolawole']
# joined = " ".join(mynamelist)
# print(joined)

#write a program to change "I am a boy" to "i-am-a-boy"

# wordbank = 'i am a boy'
# wordsplit = wordbank.split()
# jointword = "-".join(wordsplit)
# print(wordsplit)


# wordd = 'i am a boy'.replace(" ","-")
# print(wordd)




# QUESTIONS - 
# WRITE A PROGRAM THAT TAKES USER INPUT, SEARCHES FOR IT AND RETURNS STRING WITH USER INPUT
#  CAPITALIZED AND TELL USER HOW MANY TIMES THE WORD APPEARED



# soln - a word is given and the program must first 'find' that word then it would capitalize the word and return the whole lyrics
# 


# perelyrics = """Cos i want to dance with you pere 
# omo ma lo ro pe mo pERE if your boyfriend 
# call me ma PERE""".upper()

# print(perelyrics)
# lyrics = input('input your search: \n')
# print(lyrics)
# print(perelyrics.count(lyrics))



# lyrics = input('input your search').replace() 
# print(perelyrics.find(''))
# print(perelyrics.find('a')).upper()



#Given two strings s1 and s2 create a new string by appending s2 in middle of s1 and expected output should be "Aukellylt"


# strip removes spaces before or after a string





