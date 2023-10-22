import collections
from collections import deque

"""data deque is pronounced data dek
why deque?
faster in terms of adding elements to the 
end and beginning of a list
if you wish to add elements to the end and 
beginning of a list, instead of using a for loop
you deque"""

d = deque("hello")
print(d)

# add elements to the deque
d.append("5")
print(d)
print(d.append(5))
print(d)
print(d.appendleft(4))
print(d)

# remove elements:
print(d.pop())
print(d)
# removes first element:
print(d.popleft())
print(d)

# remove everything from the deque
d.clear()
print(d)

# extend: takes an iterable argument(list, string, etc) and
# adds it to the end of the list
d.extend("456")
print(d)
d.extend([1,2,3])
print(d)
d.extend('hello')
print(d)
d.extendleft('hey')
print(d)

# rotate: takes an integer, if positive rotate all element by that integer to the right
# if negative, rotate all of them by that to the left
d.rotate(-1)
print(d)
d.rotate(1)
print(d)
d.rotate(4)
print(d)

d.clear()
# when initiating a deque, if you specify maxlen
d = deque("hello", maxlen=5)
print(d)
d.append(12)
print(d)
d.extend([1,2,3])
print(d)

# reverse
d.reverse()
print(d)

