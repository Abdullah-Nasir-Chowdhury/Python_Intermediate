li = [1,2,3,4,5,6,7,8,9,0]

def func(x):
    return x**x

newList = []
for x in li:
    newList.append(func(x))

print(newList)

# using map function:
"""using map function allows the user to make use of a function
the function takes in two positional arguments: the function and the variable for the function"""
print(f"using map function: {list(map(func,li))}")

# list comprehension:
print([func(x) for x in li])
print([func(x) for x in li if x%2 == 0])
# get object description:
print([(func(x) for x in li)])