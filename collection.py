mylist=[23,32,43,43,54,543,345,364]

print(mylist)
print(mylist[1:3])
print(mylist[0:3])
print(mylist[3:])
print(mylist[1::2])
print(mylist[8::-1])
print(mylist[8:5:-1])

mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

mylist.insert(3,1234)
print(mylist)

mylist.extend([98,89,60])
print(mylist)

mylist.remove(43)
print(mylist)