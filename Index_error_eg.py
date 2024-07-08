# Example of index error

subject = ['java','python','c++','android','html']
print(subject)

a = input('Enter the name of subject from list: ')
b = int(input('Enter the index from the subject list: '))


try :
    x = subject.index(a) 
    print('The subject is at index: ',x)
    print('Value of given index from subject is: ',subject[b])
    
    
except (ValueError,IndexError) :
    print('The subject is not in the list')
    
              