#Operations with sets, mainly used in databases manipulation

#Union
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
print(my_set3)


#Intersection
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 & my_set2
print(my_set3)


#Diference
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 - my_set2
print(my_set3)
my_set4 = my_set2 - my_set1
print(my_set4)


#Simetric diference
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 ^ my_set2
print(my_set3)






