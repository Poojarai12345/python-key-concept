from xml.dom.minidom import Element


def outer (state):
    element =state
    print('element in outer ',state)
    def inner (data):
        inside=data
        print('element in inner ',element)
        print('element in inside ',state)
    inner ('first call')

    return inner

outer ("Strong")    