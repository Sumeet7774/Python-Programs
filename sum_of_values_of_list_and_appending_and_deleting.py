# Sum of the values of list and appending

list = [10,20,30,40,50]
s = 0

for i in list:
    s += i
    
list.append(s)
print(list)

list.pop(3) 
print(list)   

