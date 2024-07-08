# Appending the list

list1 = [0,1,2,3,4,5]
list2 = [10,20,30,40,50]

# list3 = list1 + list2

# print(list3)

list1.append(list2)     #we have used append function to append list2 into list1
print(list1)

list1.append(list2[2])  #we have used append function to append the index 2 of list2 into list1
print(list1)


