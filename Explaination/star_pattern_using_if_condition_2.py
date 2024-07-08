# *****
# ****
# ***
# **
# *


num = int(input('Enter your number: '))

# this pattern is done using range

# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(' * ',end='')
#     print('')    


# this pattern is done using if condition

for i in range(1,num+1):
    for j in range(1,num+1):
        if j >= i:
            print('*',end='')
    print('') 

    
    
    