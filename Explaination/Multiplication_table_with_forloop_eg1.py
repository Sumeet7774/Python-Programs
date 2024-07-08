# Multiplicaion table using for loop

a = int(input('Enter your number: '))


print('The multiplication table of %d is ' %(a))
for x in range(1,11):
    print(a,' * ',x,' = ',a*x)
    
print('')    

print('Square table of upto %d is ' %(a))
print('     NO      |       SQUARE ')
for x in range(1,a+1):
    print('       ',x,'    =     ',x*x)
    
      
  