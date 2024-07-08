# List manipulation using function

sports = []

def display(sports):
    print('Values of sports list are: ')
    for i in sports:
        print(i,end=' ')
    print('')
        
def add(sports):
    a = input('Enter your sport name: ')
    sports.append(a)
    
print('1. Displaying Sports List')
print('2. Adding Sports List')

while(1):
    choice = int(input('Enter your choice: '))
    if choice == 1:
        display(sports)
    elif choice == 2:
        add(sports)
        print('Values added successfull in the list')
    else:
        break







