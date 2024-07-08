# Stack using dequeue
# dequeue is a data structure similar to stack. It will remove last element 

from collections import deque

dq = deque()
print(type(dq))

dq.append('Football')
dq.append('Baseball')
print('after appending : ',dq)


dq.pop()
print('after removing : ',dq)

























