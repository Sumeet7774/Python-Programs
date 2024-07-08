#The greatest of 3 numbers

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

if a > b :
    if a > c:
        print('a is greater')
    else :
        print('c is greater')
elif b > a:
    if b > c:
        print('b is greater')
    else : 
        print('c is greater')
elif c > a:
    if c > b :
        print('c is greater')
    else :
        print('b is greater')
else :
    print('a is greater')        

    
    

    
         


        