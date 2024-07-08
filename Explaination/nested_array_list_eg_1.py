a = [10,20,30,40]   
b = [5,10,20,30]
c = [32,37,41,23]
d = [15,25,35,45]

arr = [a,b,c,d]     #integer declaration for array list
                    #the letter 'a' will contain all the elements of a as displayed above

print(arr[0])       #it will display all the elements of 'a' list
print(arr[3])       #it will display all the elements of 'd' list

print('To print value of a: ',arr[0][2])    #to print third value of a array list
print('To print value of c: ',arr[2][3])    #to print fourth value of c array list

print('To print value of b and c: ',arr[1:3])       #to print b and c list 
print('To print value of d after 25: ',arr[3][2:])  #to print the values of d after 25

print(arr[1][-3])   #to print the value of 10 from b list using negative index


