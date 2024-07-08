#     *
#    **
#   ***
#  ****
# *****


num = int(input('Enter your number: '))

for i in range(1,num+1):
    for space in range(1,(num+1)-i):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print('')        
        
        
        
