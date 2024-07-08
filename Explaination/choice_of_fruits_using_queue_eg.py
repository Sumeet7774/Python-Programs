# Implementation of fruits using queue
# fruits queue


from queue import Queue as q

fruits = q(maxsize = 5)
print('-----------The choices are: ---------- ')
print('1. Put')
print('2. Get')
print('3. Exit')

while(1):
    print('')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        if fruits.full() == False:
            a = input('Enter fruit name: ')
            print('')
            fruits.put(a)
        else:
            print('Fruit list is full')
    elif choice == 2:
        if fruits.empty() == False:
            print('')
            print(fruits.get())
        else:
            print('')
            print('Fruit list is empty')
    else:
        break
            
        
        
        
        







