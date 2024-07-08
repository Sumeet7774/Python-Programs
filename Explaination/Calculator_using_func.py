# Calculator using function

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))


def addition(num1,num2):
	ans = num1 + num2
	print('Addition is: ',ans)

def substraction(num1,num2):
	ans = num1 - num2
	print('Substraction is: ',ans)

def multiplication(num1,num2):
	ans = num1 * num2
	print('Multiplication is: ',ans)
	
def division(num1,num2):
	ans = num1 / num2
	print('Division is: ',ans)

print('Enter your choices: 1 to 4')
print('1. Addition')
print('2. Substraction')
print('3. Multiplication')
print('4. Division')

choice = int(input('Enter your choice: '))

if choice == 1:
	addition(num1,num2)
elif choice == 2:
	substraction(num1,num2)
elif choice == 3:
	multiplication(num1,num2)
else:
	division(num1,num2)
