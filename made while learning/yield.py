def sayac():
    n = 1
    while n <= 3:
        yield n
        n += 1


    
for i in sayac():
    print(i)

def infinite_counter():
    n = 0 
    while True:
        yield n 
        n += 1


for i in infinite_counter():
    print(i)


def test():
    print("1. adım")
    yield 10
    print("2. adım")
    yield 20
    print("3. adım")
    yield 30


g = test()

next(g)
next(g)
next(g)


def gen():
    i = 0 
    while True:
        yield i 
        i += 1



def infinite_counter():
    n = 0
    while True:
        yield n 
        n += 1


        



















































