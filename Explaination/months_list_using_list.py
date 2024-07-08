# Months list using list

question = ['What month you were born?']
option = ['January','February','March','April','May','June','July','August','September','October','November','December']
answer = ['G']
choice = ['A','B','C','D','E','F','G','H','I','J','K','L']
marks = 0
total_marks = 1

for i in range(0,1):
    print(question[i])
    
    for j in range(0,12):
        print(choice[j],'',option[j])       
    print('')   
    
    ans = input('Enter your choice of answer: ')   
    
    if ans == answer[i] or ans == answer[i].lower():
        print(option[6],'is a very good month.In This month we get rain')
    else: 
        print('Your are unlucky go die')




            
        
        