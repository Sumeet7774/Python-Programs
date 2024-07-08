#  To check if the number is palindrome or not for number
# or to reverse the number


num = int(input('Enter your number string: '))
rev = 0
original = num 

while(num!=0):
    rem = num % 10
    rev = rev * 10 + int(rem)
    num = int(num / 10) 
else:
    print('Out of while block when num value is 0')
    
print('')    
print('Reverse is: ',rev)
    

if original == rev:
    print('It is a Palindrome')
else:
    print('It is not a palindrome number')    




