#  Alphabet storing in a comprehension list

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')

alpha = ''

print('ASCII value of A is : ',A)
print('ASCII value of Z is : ',Z)
print('ASCII value of a is : ',a)
print('ASCII value of z is : ',z)
print('')

up = [chr(i) for i in range(A,Z+1)]
low = [chr(i) for i in range(a,z+1)]

print('Upper case alphabet string is: ',up)
print('')
print('Lower case alphabet string is: ',low)










