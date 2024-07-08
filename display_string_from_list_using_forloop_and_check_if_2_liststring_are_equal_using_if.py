# Displaying value of string list and checking if 2 list are equal using if 

hobby1 = ['Football','Cricket','Basketball','MMA','Hockey']
hobby2 = ['Tennis','Football','Boxing','MMA','Golf']
print(hobby1)
print(hobby2)

for x in hobby1 :
    print('The Hobbies is: ',x)
    
print('')    
    
for x in hobby2 :
    print('The Hobbies is: ',x)    
    
print('')    
    
if hobby1 == hobby2 :
    print('All hobbies are equal')
else : 
    print('None of them are equal')



if hobby1[3] is hobby2[3] :
    print('They are equal')
else:
    print('They are not equal')    
    
    
    