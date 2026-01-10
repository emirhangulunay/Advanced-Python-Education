def strike(text):
    return ''.join(c + '\u0336' for c in text)

def underline(text):
    return ''.join(c+ '\u0332' for c in text)


def overline(text):
    return ''.join(c + '\u0305' for c in text)


def midline(text):
    return ''.join(c + '\u0335' for c in text)

def strike_underline(text):
    return ''.join(c + '\u0336' + '\u0332' for c in text)


def stylize(text, effect):
    effects = {
        "strike": '\u0336',
        "underline": '\u0332',
        "overline": '\u0305',
        "midline": '\u0335'
    }

    mark = effects.get(effect)
    
    if not mark:
        return text
    return ''.join(c + mark for c in text)

print(stylize("emir", "strike"))
print(stylize("emir", "underline"))
print(stylize("emir", "overline"))
print(stylize("emir", "midline"))


import random

def zar():
    return random.randint(1,6)

it = iter(zar, 6)

for i in it:
    print(i)



f = open("data.txt", "r")

it = iter(f)

print(next(it))

print(next(it))


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    
    def __iter__(self):
        return iter(range(self.start, self.end))
    

mr = MyRange(5,10)

for x in mr:
    print(x)



#iterator kopyalanamaz
it = iter([10,20,30])

it2= it

print(next(it))

print(next(it2))


s = {1, 2, 3}

it = iter(s)

print(next(it))
print(next(it))
print(next(it))


def infinite():
    while True:
        yield "sonsuz..."


it = iter(infinite())


print(next(it))

print(next(it))


d = {"a":1, "b":2}

it = iter(d)

print(next(it))
print(next(it))

def generate():
    return random.randint(1, 10)


it = iter(generate, 7)

for n in it:
    print(n)

nums = [10, 20, 30, 40]
it = iter(nums)

for x in it:
    print(x)

    if x == 20:
        print(next(it))

from collections import deque
q = deque([1,2,3,4])

def pop_left():
    try:
        return q.popleft()
    
    except IndexError:
        raise StopIteration
    

it = iter(pop_left, StopIteration)


for x in it:
    print(x)

#!!!!!!!!!!!!!!
def infinite_even_numbers():
    n = 0
    while True:
        yield n
        n += 2


it = iter(infinite_even_numbers())

print(next(it)) 
print(next(it)) 
print(next(it)) 


class Infinite:
    def __iter__(self):
        return self
    
    def __next__(self):
        return "never ending"



it = iter(Infinite())

for i in range(5):
    print(next(i))

class WordByWord:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        
        word = self.words[self.index]

        self.index += 1

        return word
    

sentence = WordByWord("Python iter olayı çok tatlı")

for w in sentence:
    print(w)

class Squares:
    def __init__(self, limit):
        self.limit = limit
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        
        val = self.n ** 2

        self.n += 1

        return val
    

for x in Squares(5):
    print(x)



def fake_api():
    for page in range(1, 4):
        yield f"page {page} data"


data = iter(fake_api)


print(next(data))
print(next(data))
print(next(data))











































