# Sublist of list using comprehension

sports = ['Football','Cricket','Baseball','Tennis','MMA']
print(sports)
print('')

a = input('Enter your first sports name: ')
b = input('Enter your second sports name: ')

comp = [r for r in sports if r.lower() != a.lower() and r.lower()  != b.lower()]
print('Using Comprehension')
print(comp)
print('')

print('Using simple method')
s1 = []
for r in sports:
    if r.lower() != a.lower() and r.lower() != b.lower():
        s1.append(r)
print(s1)

    



 