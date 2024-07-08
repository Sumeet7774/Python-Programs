# Find factorial of all nth term using function and for loop

def factos(i):
    ans = 1
    for n in range(1,i+1):
        ans *= n
    print(ans,end=' ')

num = int(input('Enter your number: '))
print('')
print('------The factorial of nth term is------')
for i in range(1,num+1):
    factos(i)

