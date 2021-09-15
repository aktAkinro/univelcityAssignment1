s1 = "Ault"
s2 = "Kelly"

index = s1.find('l')
final_string = s1 [: index] + s2 + s1[index:]
print(final_string)


ss1 = "America" 
ss2 = "Japan"

index = ss1.find('m')
final_stringg = ss1 [0:1] + ss2 [0:1] + ss1 [3:4] + ss2 [2:]
print(final_stringg)


sss1 = "Abc"
sss2 = "Xyz"

final_stringg = sss1 [0:1] + sss2 [-1:] + sss1 [1:2] + sss2 [-2:-1] + sss1 [2:3] + sss2 [-3:-2]
print(final_stringg)