# List example to take value from user in empty list 

student = [[],[]]       #here the first list is at index 0 and second list is at index 1

#here first list is for student name 
# And second is for student course



# student[0].append('Mitesh') 
# student[1].append('CE')

# student[0].append('Sumeet') 
# student[1].append('10 Pass')

# print(student)


num = int(input('Enter your number: '))

for i in range(0,num):
    name = input('Enter your name: ')
    branch = input('Enter your branch: ')
    student[0].append(name)
    student[1].append(branch)
print(student)
        



