# even odd pattern

num = int(input('Enter the num: '))
 
#for printing the even numbers

for i in range(0,num):
    if i % 2 == 0:
        print(i)
        
print('Now we are printing odd number:::::')

#for printing the odd numbers

for i in range(0,num):
    if i % 2 != 0:   
        print(i)
