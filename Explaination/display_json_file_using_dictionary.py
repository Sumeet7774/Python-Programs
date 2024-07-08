# Displaying json file using dictionary format

quiz = { 'Q1': {
                'Which is our national animal?':['Peacock','Tiger','Elephant','Lion'],
                'correct':'Tiger'
               },
        
         'Q2':{
               'Which is our national Bird?':['Peacock','Tiger','Elephant','Lion'],
               'correct':'Peacock'
              },
         
         'Q3':{
                 'Which player plays for Fc Barcelona?':['Muller','Lewandowski','Kevin De Bruyne','Neymar','Halland'],
                  'correct':'Lewandowski'
              }  
       } 


# print(quiz['Q1']['Which is our national animal?'])
# print(quiz['Q2']['Which is our national Bird?'])
# print(quiz['Q3'][Which player plays for Fc Barcelona?'])


# print(quiz['Q1']['correct'])
# print(quiz['Q2']['correct'])
# print(quiz['Q3']['correct'])


for key in quiz:            #here it will hold main key of dictionary such as Q1 and Q2
    print(key,' : ',end='')
    for i in quiz[key]:     #here it will hold keys of nested dictionary for eg 'Which is our national animal?',correct and 'Which is our national Bird?',correct           
        print(i)
        for j in quiz[key][i] :     #here it will hold option of nested dictionary
            if (i != 'correct'):    #here it will not traverse value of 'correct' as new character 
                print('     ',j)
            else:   
                print(j, end='')
        print('')
    print('')        
        
    
    
    
    


