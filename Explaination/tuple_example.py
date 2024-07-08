# Example of Tuple

fruit = ('Mango','Orange','Strawberry','Pineapple','Apple')
vegetable = ('Cabbage','Cauliflower','Carrot','Potato')


print('Tuple is: ',fruit)
print('The datatype is: ',type(fruit))
print(fruit[-1])
print(fruit[0:3])

# fruit[3] = 'Pomegranate'    #tuple is not changeable or updatable 
# print(fruit)

print(fruit + vegetable)
food = fruit + vegetable
print(food)

for i in food:
    print(i)
    
    
dishes = ['Punjabi','Pizza','Burger','Hot Dog']  
a = tuple(dishes)       #this will convert from list to tuple
print('Conversion of list to tuples: ', a)

a = list(fruit)       #this will convert from tuple to list
print('Conversion of tuples to list : ', a)






