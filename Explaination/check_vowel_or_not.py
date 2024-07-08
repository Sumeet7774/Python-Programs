# Program to check whether the entered character is vowels or not(consonant)

char = input('Enter your vowel character or number: ')

if char.upper() == 'A' or char.upper() == 'E' or char.upper() == 'I' or char.upper() == 'O' or char.upper() == 'U':
    print('Your character is a vowel')
else:
    print('Your character is not a vowel')    

print('')
print('-----------Category of alphabet------------')

if (char >= 'A' and char <= 'Z'):
    print('Upper alphabet')
elif (char >= 'a' and char <= 'z') :
    print('lower alphabet')
elif (char >='0' and char <= '9' ):
    print('It is a number')
else:
    print('It is a special character')








