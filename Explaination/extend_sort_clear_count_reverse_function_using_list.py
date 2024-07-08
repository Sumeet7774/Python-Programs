# Explaining the use of extend,sort,clear,count,reverse function
# Appending values of another list to specific list

fruit = ['Mango','Orange','Banana','Orange']
dryfruit = ['Almond','Cashew','Nut']

# fruit.append(dryfruit)
# print('By appending: ',fruit)

#extend function
fruit.extend(dryfruit)      # Use of Extend function is to append values of another list to specific list(iteration) meaning it will merge the values
print('By extending: ',fruit)
print('')


#count function     #count function is use to count the duplicate values of the list
print('')
cnt = fruit.count('Orange')
print('Counting of the values of list: ',cnt)
print('')


#reverse function
fruit.reverse()         #reverse function is used to reverse the values of list
print('')
print('Reverse of list is: ',fruit)
print('')



#sort function
print('Unsorted list: ',fruit)
fruit.sort()    #here the sort function sort the values of list in ascending order
print('Sorted list: ',fruit)

print('')
print('Fruit element using iteration')
for i in fruit:
    print(i)
 
    
 
#clear function 
print('')    
fruit.clear()   #clear function here clears all the values of fruit
print('All elements deleted list fruit ::',fruit)



