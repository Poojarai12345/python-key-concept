def fun():
    print('funny function')

temp= fun

print(temp)
print(fun)
print(type(temp))
print(type(fun))
print(temp==fun)
