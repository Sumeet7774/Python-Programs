#Calculator using if statement and list

l = [1,2,3,4]           #it is the choices of op
op = ['Addition','Subtraction','Multiplication','Division'] #it is the operation to be performed

a = int( input('Enter your value: ') )  #type conversion from string to integer

b = int( input('Enter your second value: ') )   #type conversion from string to integer

print(l[0],' : ',op[0])
print(l[1],' : ',op[1])
print(l[2],' : ',op[2])
print(l[3],' : ',op[3])

c = int( input('\nEnter your choice: ') ) 

if c == l[0]:
    print(op[0],' is: ',a+b)
elif c == l[1]:
    print(op[1],' is: ',a-b)
elif c == l[2]:
    print(op[2],' is: ',a*b)
else :
    print(op[3],' is: ',a/b)
    



    
    
    
    
    





