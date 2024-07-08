# User input find nth even number using function and for loop

def even(num):
    if num % 2 == 0:
        print(num , end=' ')

num = int(input('Enter your number: '))

for i in range(1,num+1):
    even(i)