# create set1 of int type

age = input("how old are you? ")
weight = input("how many kgs are you? ")
height = input("how tall are you? ")

set1 = {age, weight, height}
print(set1)

# create set2 ofint type
shoe_size = input("what is your shoe size? ")
waist = input("what is waist size? ")
shoulder  = input("what is your shoulder size?  ")

set2 = {shoe_size, waist, shoulder}
print(set2)

set1.update(set2)
print(set1)