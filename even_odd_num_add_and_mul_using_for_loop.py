# Odd number addition and multiplication

num = int(input('Enter your number: '))

c = 0

for i in range(0,num):
    if i % 2 == 0:
        print(i)
     
print('')        
        
for i in range(0,num):
    if i % 2 != 0:
        print(i)        
        
    
for i in range(0,num):
    if i % 2 != 0:
       c += i
print('The sum of odd numbers is: ',c) 

mul = 1

for i in range(1,num):
    if i % 2 != 0:
        mul *= i
print('The multiplication of odd numbers is: ',mul) 


for i in range(0,num):
    if i % 2 == 0:
       c += i
print('The sum of even numbers is: ',c)


mul = 1

for i in range(1,num):
    if i % 2 == 0:
        mul *= i
print('The multiplication of even numbers is: ',mul)        

       