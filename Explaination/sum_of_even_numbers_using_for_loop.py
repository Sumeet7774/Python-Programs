# sum of even numbers using for loop

num = int(input('Enter your number: '))
c = 0

for i in range(0,num):
    if i % 2 == 0:
        print(i)


for i in range(0,num):
    if i % 2 == 0 :
        c += i
print('The sum of even numbers is: ',c)

