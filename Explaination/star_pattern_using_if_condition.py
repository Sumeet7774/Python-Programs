# *
# **
# ***
# ****
# *****

num = int(input('Enter your number: '))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('* ',end='')
#     print(' ')    
    
for i in range(1,num+1):
    for j in range(1,num+1):
        if (j <= i):
            print(' * ',end='')
    print(' ')         
            
            
    
    