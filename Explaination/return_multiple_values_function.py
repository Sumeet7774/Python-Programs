# Return Multiple values using return type function

def cal(a, b):
    return a + b, a - b, a * b, a / b


add, sub, mul, div = cal(10, 5)
print(' Addition is ', add, '\n Subtraction is: ', sub, '\n Multiplication is: ', mul, '\n Division is: ', div)




