#Example of value error

subject = ['java','python','c++','android','html']
print(subject)

a = input('Enter your subject: ')

try : 
    print('Your subject is at index',subject.index(a),'found in the list')
    
except ValueError:
     print('Your subject is not found in the list of subjects')

    
    