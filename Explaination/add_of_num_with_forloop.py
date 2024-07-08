# Addition of 1 to n numbers
c = 0
num = int(input('Enter your number: '))


for i in range(1,num+1) :
    c += i

print('The sum of upto %d is %d ' %(num,c))
