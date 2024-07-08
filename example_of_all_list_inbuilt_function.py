# Example to use all function of list

sports = ['Football','Boxing','MMA','Baseball']
fruit = ['Orange','Apple','Mango','Mango','Banana']

sports.extend(fruit)
print('After extending the list is: ',sports)
print('')

sports.sort()
print('After sorting the list is: ',sports)
print('')

cnt = fruit.count('Mango')
print('Total number of repeated item in list is: ',cnt)
print('')

sports.reverse()
print('After reversing the list is: ',sports)
print('')

sports.insert(3,'Tennis')
print('After inserting the list is: ',sports)
print('')

sports.clear()
print('After clearing the list is: ',sports)
print('')
