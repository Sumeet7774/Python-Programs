# explaination of zero division error using try except

a = 10
b = 0

try:
    print( a/b)

except ZeroDivisionError:
    print('You cannot divide a number by zero')
