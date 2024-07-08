# To print the prime numbers till number given by user

num = int(input('Enter your number: '))

count = 3
prime = 0
i = 2

print('Prime numbers are: ',end=' ')

while(i<=num):
    for j in range(2,count):
        if count % j == 0:
            prime = 1
            break
        else:
            prime = 0
    else:
        print(count,end=' ')
        i += 1
    count += 1
       



