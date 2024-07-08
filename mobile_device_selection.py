# Index example of mobile order

mobile = ['Apple','Mi','Samsung','Samsung','Nokia']
print(mobile)

a = int(input('Enter the index of the mobile company from the list: '))

        
try:
    print('Value of given index from mobile is: ',mobile[a])
    
except (ValueError,IndexError):
    print('The index of the company is not present in the list')
    
        