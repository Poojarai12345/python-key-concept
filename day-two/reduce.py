from functools import reduce

listx=[23,43,456,654,25,85,63,85]

result = reduce(lambda x,y:x+y, listx)
print(result)

result= reduce(lambda x,y: x if x>y else y,listx)
print(result)