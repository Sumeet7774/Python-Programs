# Voting of multiple user using condition(if) and list

name1 = input('Enter your name: ')
name2 = input('Enter your second name: ')

age1 = int (input('Enter your age: '))
age2 = int (input('Enter your second age: '))


a1 = [name1, name2]
a2 = [age1,age2]
arr = [a1,a2]       #it contains the contents a1 and a2. a1 and a2 contains name1 and name2

print(arr)

if arr[1][0] > 17 :
    print(arr[0][0],' is eligible for voting')
else :
    print(arr[0][0],' is not eligible for voting')  #Here is the end of first user loop
        
if arr[1][1] > 17:
    print(arr[0][1],' is eligible for voting')      
else : 
    print(arr[1][1],' is not eligible for voting')    #Here is the end of second user loop
    

    


 