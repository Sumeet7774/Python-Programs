# mcq creating json dictionary file by manually

quiz = { 'Q1': {'Which is our national animal?':['Peacock','Tiger','Elephent','Lion'],
         'correct':'Tiger'
         },
         'Q2':{'Which is our national Bird?':['Peacock','Tiger','Elephent','Lion'],
          'correct':'Peacock'
         }
       } 


# print(type(quiz))

print(type(quiz['Q1'].values()))

for i in quiz:
    for j in quiz[i].values():
        for k in j:
            print('op: ', k)