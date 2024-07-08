# Question and answer based dictionary eg

que = {'What is your name':'Sumeet','What is your age':'18'}
ans_l = []
i = 0
count = 0

print('The keys of dictionary are: ',que.keys())    #here we are printing only the keys of dictionary
print('The values of dictionary are: ',que.values())    #here we are printing only the values of dictionary 

print('')
print('')
print('--------Displaying dictionary using forloop---------')

for key in que:
    #print(key)  #this will print all the keys of the dictionary
    ans = input(key +' : ')
    ans_l.append(ans)
      
        
    
for value in que:
    #print(que[value])    #this will print all the values of the dictionary
    if ans_l[i].upper() == que[value].upper():
        count += 1
        i += 1
print('Your total result is: ',count)

      
    















