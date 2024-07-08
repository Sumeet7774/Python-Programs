# Dictionary eg of sports

sports = {'Name':['Football','Cricket','Baseball','Tennis'],
         'Origin':['Pakistan','England','Japan','Germany'],
         'Players':['11','11','25','2'] }

idx = 0


for key in sports:
    print('-----',key)          
    for i in sports[key]:
        print('         ',i)


print('Ask question from sports name, sports origin, sports player :: ')
print('')

que1 = input('Enter your sports: ')
que2 = input('Enter to find  Sport \'origin\' Or \'players\' : ')


for key in sports:      
    for i in sports[key]:   #for finding values in sports list
        if que1.upper() == i.upper():
            idx = sports[key].index(i)  #from que1 input finding its index
            break
    break
            


for key in sports:            
    if que2.upper() == key.upper():
        for j in range(0,len(sports[key])):     #comparing by indexing of list 
            if idx == j:
                print('Value of',que2,'is  ',sports[key][j])
                
            
            
            
            
            
            
            
            









