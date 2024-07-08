# To check whether character is alphanumeric or special character
 


char = input('Enter your vowel character or number: ')

print('-----------Category of alphabet------------')

if (char >= 'A' and char <= 'Z'):
    print('Upper alphabet')
elif (char >= 'a' and char <= 'z') :
    print('lower alphabet')
elif (char >='0' and char <= '9' ):
    print('It is a number')
else:
    print('It is a special character')
    
    
    
    