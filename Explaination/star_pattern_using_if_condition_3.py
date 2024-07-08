#     *
#    **
#   ***
#  ****
# *****

# Star pattern using if condition


num = int(input('Enter your number: '))

for i in range(1,num+1):
    for j in range(1,num+1):
        if j<=num-i: 
            print('   ',end='')
        else:
            print(' * ',end='')
    print('')
    

