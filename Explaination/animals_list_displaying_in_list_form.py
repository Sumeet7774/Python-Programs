# animals list by displaying in list form

animals = []
print(animals)

for i in range(0,3):
    x = input("Enter name of an animal ")
    animals.append(x)

print('list of animals after update: ', animals)


# animals list by displaying in operator form
 
animals = []

for i in range(0,3):
    x = input('Enter your animal: ')
    animals.append(x)
    
for i in animals:
    print(i)    
    
