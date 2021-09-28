# sets are unordered and dont allow duplicates. They are changeable

# discard vs remove

# the remove() raises error when specified element doesnt exist while discard wouldnt. discard would print everything

# s = {"True", "Born", "Time", 5600}

# s.discard ("emeka")
# s.remove ("emeka")
# print(s)

# you can add an item to set using add



# set1 = {"True", "Born", "place", 5600}
# set1.add ("emeka")
# print(set1)



# union brings two sets together

# a = {"True", "Born", "place", 5600}
# b = {"True", "orn", "plce", 5}


# u = a.union(b)
# print(u)


# intersection gives us two similar things but if nothing is similar it gives empty set

# q = {"True", "Born", "place", 5600}
# e = {"True", "orn", "plce", 5}

# qe = q.intersection(e)
# print(qe)



# set difference
# set a = {10,20,30,40}
# set b = {1,2,30,40}

# set a - b = {10,20} the elements in a that are not in b
# set b - a = {1,2} the elements in b that are not in a 


# set update doesnt create a new variable like union would, it just adds the value from one to the other.

# q1 = {"True", "Born", "place", 5600}
# e1 = {"True", "orn", "plce", 5}

# q1.update(e1)
# print(q1)


# symmetric difference is (a-b) union (b-a). union of the differences between two variables. 
# everything they dont have in common

# d = {"True", "Born", "place", 5600}
# f = {"True", "orn", "place", 5}

# print(d.difference(f))
# print(f.difference(d))
# print(d.symmetric_difference(f))



# pop in sets picks out values randomly





# retun a new set of identical items from a given two set


# g = {10,20,30,40,50}
# y = {30,40,50,60,70}

# gy = g.intersection(y)
# print(gy)

# 
# g1 = {10,20,30,40,50}
# y1 = {30,40,50,60,70}

# print(g1.difference(y1))
# print(y1.difference(g1))
# print(g1.symmetric_difference(y1))




# given twwo python sets update the first with items that exist only in first set and not in second
# set1 = {10,20,30}
# set2 = {20,40,50}

# print(set1.difference_update(set2))****


# remove items 10,20,30 from set at once
# set123 = {10,20,30,40,50}

# set123.difference_update({10,20,30})

# print(set123)


# return a set of all elements in either A or B but not both
# set11 = {10,20,30,40,50}
# set12 = {30,40,50,60,70}


# print(set11.difference(set12))
# print(set12.difference(set11))
# print(set11.symmetric_difference(set12))


# check if two sets have any elements in common. if yes, display the common elements



# remove items from set 1 that are not common to both set1 and set2

# k = {10,20,30,40,50}
# l = {30,40,50,60,70}

# print(k.difference(l))


# learn update*******



# english = {1,2,3,4,5,6,7,8,9}
# french = {10,1,2,3,11,21,55,6,8}

# # print(english.difference(french))
# # print(french.difference(english))

# new = french.symmetric_difference(english)

# print(len(new))


















