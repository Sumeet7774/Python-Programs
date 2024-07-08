# Voting of multiple user(3 users) using if(condition) and list

name1 = input('Enter first name: ')
name2 = input('Enter second name: ')
name3 = input('Enter third name: ')

print('')

age1 = int(input('Enter age of first person: '))
age2 = int(input('Enter age of second person: '))
age3 = int(input('Enter age of third person: '))

a1 = [name1,name2,name3]
a2 = [age1,age2,age3]
arr = [a1,a2]       #it contains all the elements of a1 and a2... as a1 and a2 contains name and age, this list contains all the elements 

print(arr)
print('')

if arr[1][0] > 17 :
    print(arr[0][0],' is eligible for voting')
else :
    print(arr[0][0],' is not eligible for voting')

if arr[1][1] > 17 :
    print(arr[0][1],' is eligible for voting')
else :
    print(arr[0][1],' is not eligible for voting') 
    

if arr[1][2] > 17 :
    print(arr[0][2],' is eligible for voting')
else :
    print(arr[0][2],' is not eligible for voting')     
    
    