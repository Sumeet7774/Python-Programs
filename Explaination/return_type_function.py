# Mathematical function using function return type

def cube(n):
    return n * n * n


def expo(a, n):
    return a ** n


def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def grade(n):
    if (n >= 85) and (n <= 100):
        return 'A grade'
    elif (n >= 70) and (n < 85):
        return 'B grade'
    elif (n >= 50) and (n < 70):
        return 'C grade'
    else:
        return 'Failed'


choice = 0
print('1. Cube')
print('2. Exponentiation')
print('3. Greatest number')
print('4. Grade System')

choice = int(input('Enter your choice: '))
print('')
if choice == 1:
    ans = cube(5)
    print('The cube is: ',ans)
elif choice == 2:
    ans = expo(2, 5)
    print('The exponentiation is: ', ans)
elif choice == 3:
    ans = greater(10, 15, 5)
    print('The greatest number is: ', ans )
else:
    ans = grade(70)
    print('The grade is: ', ans)

