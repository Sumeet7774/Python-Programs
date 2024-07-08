# Example of mod, floor and exponent number using assignment operators

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

c %= a
print('The mod is: ',a)

b //=a 
print('The floor is: ',b)

c **=a
print('The exponent is: ',c)
