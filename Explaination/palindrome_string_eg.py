# To check if the string is palindrome or not for string

string = input('Enter your string: ')
length = len(string)
rev=''


for i in range(1,length+1):
    rev = rev + string[length-i]
print(rev)

if string == rev:
    print('It is a Palindrome')
else:
    print('It is not a palindrome number')    

