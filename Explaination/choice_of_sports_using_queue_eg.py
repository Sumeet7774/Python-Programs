# Implementation of sports using queue
# sports 


from queue import Queue as q
sports = q(maxsize=5)
print('-----------The choices are: ---------- ')
print('1. Put')
print('2. Get')
print('3. Exit')

while(1):
    print('')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        if sports.full() == False:
            a = input('Enter sports name: ')
            print('')
            sports.put(a)
        else:
            print('Sports list is full')
    elif choice == 2:
        if sports.empty() == False:
            print('')
            print(sports.get())
        else:
            print('')
            print('Sports list is empty')
    else:
        break









