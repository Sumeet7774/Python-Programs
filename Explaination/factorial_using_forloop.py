# Factorial of n numbers

a = int(input('Enter your number: '))
c = 1

for x in range(1,a+1):
    c *= x
    
print('The factorial of %d is: %d' %(a,c))    