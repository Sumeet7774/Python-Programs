# MCQ quiz using list

question = ['Who is the best footballer of all time?','Which is the best football club of all time?']
option = [['Maradona','Ronaldinho','Cristiano','Messi','Pele'],['Fc Bayern','Juventus','Fc Barcelona','Real Madrid','Ac Milan']]
answer = ['D','C']
choice = ['A','B','C','D','E']
marks = 0
total_score = 2


for i in range(0,total_score): 
    print('')
    print('Que : [',i+1,']',question[i].upper())    #upper() 
    
    for j in range(0,5):
        print('      [',choice[j],']',option[i][j])
    
    ans = input('Enter your correct answer: ')
    if ans == answer[i] or ans == answer[i].lower():   #.lower() function is used to convert the uppercase string into lowercase
        print('Your answer is correct')
        marks += 1
    else:
        print('Correct answer is: ',answer[i])
        
print('Your total marks is: ',marks)      
 
if marks == total_score :
    print('Your performance was Excellent')
else:
    print('You are detained ')        
      
        

