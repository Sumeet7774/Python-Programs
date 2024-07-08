# Example of even number using list comprehensions

a = [1,2,3,4,5]
print('list is ',a)
print('')


simple = []
print('Using simple method')
for i in a:
   simple.append(i+i)
print(simple)
print('')


print('using comprehension  list method')
comp = [i+i for i in a ]        # here we append value of i+i in empty comprehension list using for loop
print(comp)


