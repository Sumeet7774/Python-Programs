# Multiplication table with for loop

a = int(input('Enter your number for multiplicaion table: '))
print('The multiplication table of %d is: ' %(a))


for x in range (1,11) :
    print(a,'  *  ',x,'    =    ', a*x)
    