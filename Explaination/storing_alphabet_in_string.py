# Alphabet storing in a string

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')

alpha = ''

print('ASCII value of A is : ',A)
print('ASCII value of Z is : ',Z)

print('ASCII value of a is : ',a)
print('ASCII value of z is : ',z)


up =''
low =''

for i in range(A,Z+1) :
    up += ' '+chr(i)
print('Upper case alphabet string is: ',up)

for i in range(a,z+1) :
    low += ' '+chr(i)
print('Lower case alphabet string is: ',low)










