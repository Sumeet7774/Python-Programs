# Check whether the number is prime number

num = int(input('Enter your number: '))
prime = 1

for i in range(2,num):
    if num % i == 0:
        prime = 0
        break
else:
    prime = 1
    
if prime == 1 and num != 1:
    print('It is a prime number')
else:
    print('It is not a prime number')    
        





