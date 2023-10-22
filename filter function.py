def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,0]
print(a)
"""
# it's filtering out elements based on a pre-defined function
# depending on whether the output is true or false"""
b = list(filter(isOdd,a))
print(b)
"""This is so much better than having to do a for loop
filter and map function go hand in hand"""

# this is how you use filter and map
c = list(map(add7,filter(isOdd, a)))
print(c)
# nothing new, just doing the same thing
d = list(map(add7, b))
print(d)