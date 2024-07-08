# To display months in order using list 


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']


months.sort()   #this will print the months in ascending order
print('List After Sorted',months)
print('')

print('Even months are :: ')
for i in months:
    flag = months.index(i)
    if flag % 2 == 0:
        print(months[flag])

print('')
print('Odd months are :: ')
for i in months:
    flag = months.index(i)
    if flag % 2 == 1:
        print(months[flag])
        
print('')

print('Using range Even months are :: ')
for i in range(0,12):
    if i % 2 == 0:
        print(months[i])
        
print('')        
print('Using range Odd months are :: ')
for i in range(0,12):
    if i % 2 == 1:
        print(months[i])        







