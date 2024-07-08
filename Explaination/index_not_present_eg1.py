#to find index of list using values and to use index function using exception

food = ['Pizza','Burger','Vadapav','Subway','Kachori','Sandwich']
a = input('Enter your food to find index: ')

try:
    #error generated code
    i = food.index(a)
    print('Food found at ',i,'Location')
    
    
except ValueError:
     #if the error is generated than only then only this block will be executed
     i = None
     print('Food is not found')
     print(i)

