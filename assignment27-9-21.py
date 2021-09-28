
num_qNewspaper = int(input(""))
qNewspaper = input("")
num_eNewspaper = int(input(""))
eNewspaper = input("")

f1 = set(qNewspaper.split())
f2 = set(eNewspaper.split())

final = f1.intersection(f2)
print(len(final))
print(final)



# qNewspaper = {1,2,3,4,5,6,7,8,9}
# eNewspaper = {10,1,2,3,11,21,55,6,8}

# qe = qNewspaper.intersection(eNewspaper)
# print(qe)
# print(len(qe))