# Example of division error

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
        
try : 
    c = a / b
    print('The answer is: ',c)

except ZeroDivisionError :
    print('That number is not divisible by zero')
    
    
            
        