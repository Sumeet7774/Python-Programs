# Displaying value of string list and checking if 2 list are equal using if 

subject1 = ['java','python','python','android','html']
subject2 = ['java','python','python','android','html']
print(subject1)
print(subject2)

for x in subject1 :
    print('The programming language is : ',x)
    
if subject1 == subject2:
    print('Both programming language are equal')
else :    
    print('Both programming language are not equal')


if subject1[0] is subject2[0]:
    print('Both programming language are equal')
else :    
    print('Both programming language are not equal')



#in first if condition all the list are stored in a variable so it isnt considered as string so we can use == operator
#in second if condtion we are checking only 1 list from both variable that is it equal or not. So we can use is operator when it is string


