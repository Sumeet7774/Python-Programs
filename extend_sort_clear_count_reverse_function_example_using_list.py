#Example of extend,sort,count,reverse function
# Explaining the use of extend,sort,clear,count,reverse function

sports = ['Football','Boxing','Tennis','MMA','Baseball']
fruit = ['Mango','Orange','Banana','Orange']

# fruit.append(dryfruit)
# print('By appending: ',fruit)

#extend function
sports.extend(fruit)      # Use of Extend function is to append values of another list to specific list(iteration) meaning it will merge the values
print('By extending: ',sports)
print('')


#count function     #count function is use to count the duplicate values of the list
print('')
cnt = fruit.count('Orange')
print('Counting of the values of list: ',cnt)
print('')


#reverse function
sports.reverse()         #reverse function is used to reverse the values of list
print('')
print('Reverse of list is: ',sports)
print('')



#sort function
print('Unsorted list: ',sports)
sports.sort()    #here the sort function sort the values of list in ascending order
print('Sorted list: ',sports)

print('')
print('Sports element using iteration')
for i in sports:
    print(i)
 
    
 
#clear function 
print('')    
sports.clear()   #clear function here clears all the values of fruit
print('All elements deleted list sports ::',sports)
