# To check if the number entered is prime or not

num = int(input('Enter your number: '))
prime = 0
print('2')
for i in range(2,num):
    if num % 2 == 0:
        prime = 1

if prime == 0:
    print('It is a prime number')
else:
    print('It is not a prime number')    







