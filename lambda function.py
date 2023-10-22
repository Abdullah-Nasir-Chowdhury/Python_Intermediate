"""Lambda stands for anonymous function"""

def func(x):
    return x+5

print(func(2))

func2 = lambda x: x+5
print(func2(2))

func3 = lambda *args: sum(args)
print(func3(3,4,5,6,7))

"""use lambda with map and filter"""

a = [1,2,3,4,5,6,7,8,9,0]
func4 = lambda x: x + 6
newList = list(map(func4,a))
print(newList)
# another way:
newList2 = list(map(lambda x: x+6, a))
print(newList2)

newList3 = list(filter(lambda x: x%2==0, a))
print(newList3)

