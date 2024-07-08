#Average of 4 numbers by taking input from user

a = int (input('Enter your First number: '))
b = int (input('Enter your Second number: '))
c = int (input('Enter your Third number: '))
d = int (input('Enter your Fourth number: '))

sum = 0
arr = [a,b,c,d]
print(arr)          #this will print the whole list

'''for i in arr:
#    print('values :: ',i)
     sum = sum + i

avg = sum/4

print('average using for loop : ',avg)'''

sum = arr[0]+arr[1]+arr[2]+arr[3]

avg = (sum)/4       #this will divide the sum by 4 as the sum is adding all the elements of sum
print(avg)

