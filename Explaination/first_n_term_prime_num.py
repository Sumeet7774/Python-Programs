# To print the prime numbers till number given by user


print('')

num = int(input('Enter your number: '))
prime = 0
count = 3
i = 2

print('Prime number are : 2 ',end=''  )


while(i<=num):
    for j in range(2,count) :
        if count % j == 0  :
            prime = 1
            break
        else:
            prime = 0
            
    else :
        print(count , end = ' ')
        i += 1
    count += 1  

else:
    print('')
    print('finished')
    
    






