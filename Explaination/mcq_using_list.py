# For displaying mcq using list

q = input('Enter your question: ')

op1 = input('Enter your first option: ')
op2 = input('Enter your second option: ')
op3 = input('Enter your third option: ')
op4 = input('Enter your fourth option: ')

print('\n')

cans = input('Enter the correct answer: ')

que = [q]
option = [[op1,op2,op3,op4]]

print('\n\n')

print(que)
print(option)

print('\n')

ans = input('Enter the correct option: ')


if cans is ans:
    print(ans,' is correct')
else :
    print('Correct answer is:  ',cans)    
    
    
