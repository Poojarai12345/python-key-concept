def willCallYouBack(cb):
    print("Started Working")
    cb('India')
    print('still in fun')
    cb('China')
    print('still in fun')
    cb('Russia')
    print('still in fun')
    cb('Japan')
    print('Wrapped it..')

def processIt(data):
    print('Received',data)

willCallYouBack(processIt)

#A function which is passed as parameter to another function is called a callback
