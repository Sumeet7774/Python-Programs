# To reverse the string 

string = input('Enter your string: ')
length = len(string)
rev = ''


for i in range(1,length+1):
    rev = rev + string[length-i]
print(rev)

