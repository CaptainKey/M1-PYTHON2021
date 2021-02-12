def fonction(a,b):
    print(a,b)

def fonction2(b,a=False):
    print(a,b)

def fonction3(a,b,c,**kwargs):
    print('a',a)
    print('b',b)
    print('c',c)
    print(kwargs)
    print('key',kwargs.keys())
    print('values',kwargs.values())
    for key,value in kwargs.items():
        print(key,value)

fonction2(a="toto",b="b")
fonction2(b="b")

fonction3('a','b','c',y=6,h=5,z=2)
