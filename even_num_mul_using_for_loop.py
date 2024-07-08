# Even number multiplication 

num = int(input('Enter your number: '))

c = 1

for i in range(1,num):
    if i % 2 == 0:
        print(i)
        
        
for i in range(1,num):
    if i % 2 == 0 :
        c *= i
print('The multiplication of even numbers is: ',c)        
        