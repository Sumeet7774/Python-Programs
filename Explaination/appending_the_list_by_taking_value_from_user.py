# appending the list by taking value from user
# appending the list at last

sports = ['Football','Basketball','Boxing','Tennis']
fruits = ['Apple','Mango','Banana','Orange']

print('List of fruits to add',fruits)

c = input('Enter which fruit you want to add in sports list: ')
sports.append(c)
print('')
print('Updated sports list:')


sports.pop(2)   # Pop function is used for deletion. In bracket there is index so at 2nd postion element of sports will be deleted
for i in range(len(sports)):
    print('     ',end='')
    print(i,'   ',sports[i])

