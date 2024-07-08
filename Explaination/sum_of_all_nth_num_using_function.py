# To find sum of all nth term using function

def solution(num):
    ans = 0
    for i in range(1,num+1):
        ans += i
    print(ans,end=' ')


num = int(input('Enter your number: '))
print('')
print('-------The sum for nth term is-------- ')
for i in range(1,num+1) :
    solution(i)




