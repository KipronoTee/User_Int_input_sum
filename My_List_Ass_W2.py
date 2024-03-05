# create an empty list
my_list = []

# append 4 items in the empty list 
my_list.append(10)
my_list.append(30)
my_list.append(20)
my_list.append(40)

# insert an item in the list
my_list.insert(1, 15)

# create a second list 
my_list2 = [50, 60, 70]

# extend my_list with my_list2
my_list.extend(my_list2)

# remove last item inthe updated  lsit
del my_list[-1]
my_list.sort()
print(my_list)
