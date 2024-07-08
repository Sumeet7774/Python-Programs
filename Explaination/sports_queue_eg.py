# Implementation of sports using queue

from queue import Queue as q

sports = q(maxsize = 4)     #here we declared a queue as sports with maximum size 4
print(type(sports))
print('')

sports.put('Football')  #it will add items to sports queue
sports.put('Cricket')   #it will add items to sports queue
sports.put('Baseball')  #it will add items to sports queue
sports.put('MMA')       #it will add items to sports queue
print('Sport queue is full ? : ',sports.full())     #it is a boolean value which will specify queue is full if value is true 
print('')

print('Sports queue is empty? : ',sports.empty())   #it is a boolean value which specify queue is empty if value is true
print('')


print('Displaying elements of queue : ')
for i in range(0,4):    
    print(sports.get())
    
    
print('') 
print('Sports queue is empty? : ',sports.empty())   #it is a boolean value which specify queue is empty if value is true
    
sports.put('Basketball')
sports.put('Wwe')
print(sports.get())
print(sports.get())
    
    
    
    
    
    