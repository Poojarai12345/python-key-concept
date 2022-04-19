def listprocess(list,x,y,z):
    list.extend([x,y,z])

listx=[23,32,43,54,65,456]
print(listx)
listprocess=(listx,23,34,54)
print(listprocess)

def stringprocess(name,appender):
    name+=appender
    print('within the function',name)
firstname='Rajan'
print(firstname)
stringprocess(firstname,'Rahul')
print(firstname)