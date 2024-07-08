# marks list displaying in operator form and doing sum and finding the percentage of it


marks = []
s = 0

for i in range(0,4):
    x = int(input('Enter your values: '))
    marks.append(x)
    
    
for i in marks:
    print(i)
    
s = marks[0] + marks[1] + marks[2] + marks[3] 
print('The sum of marks list is: ',s)

percentage = s / 4
print('The percentage of marks list: ',percentage)

