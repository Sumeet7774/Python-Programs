# Comprehension list of string

sports = ['Football','Cricket','Baseball','Tennis','MMA']

comp = [sports[i] for i in range(0,len(sports)) if i % 2 == 0]

print('Even sports are: ',comp)


