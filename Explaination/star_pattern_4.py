# 1 0 0
# 0 1 0
# 0 0 1

for i in range(1,4):
    for j in range(1,4):
        if i == j:
            print( ' 0 ',end='')
        else:
            print(' 1 ',end='')
    print('')        
