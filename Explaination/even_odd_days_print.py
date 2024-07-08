# Today exam 
# 24 July 2022
# Write a program to display monday,wednesday,friday,sunday if the value is 1
days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ,'sunday']

a = int(input('Enter your choice: '))

for i in range(0,7):
    if a == 1:              # 1 is for even print
        if i % 2 == 0:
            print(days[i])  
    else:
        if i % 2 != 0:      # 2 is for odd print
            print(days[i])  
