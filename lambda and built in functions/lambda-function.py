def kareAl(a):
    return a**2


sonuc = kareAl(5)

sonuc = (lambda a: a ** 2)(3)

kareAl = lambda a: a ** 2

sonuc = kareAl(4)

toplama = lambda a,b,c: a + b + c

sonuc = toplama(1,2,3)

def myFunc(n):
    return lambda a: a*n


carpma2 = myFunc(2)
carpma3 = myFunc(3)
carpma5 = myFunc(5)

sonuc = carpma2(3)
sonuc = carpma3(3)
sonuc = carpma2(3)

"""
| Topic                 | Description                      |
| --------------------- | -------------------------------- |
| What is `lambda`?     | An anonymous (unnamed) function  |
| Purpose               | Create short, one-line functions |
| Syntax                | `lambda parameters: expression`  |
| Return Statement      | Implicit (no `return` keyword)   |
| Number of Parameters  | One or more                      |
| Number of Expressions | Only one                         |
| Assignment            | Can be assigned to a variable    |
| Typical Use           | `map()`, `filter()`, `sorted()`  |
| Advantage             | Short and concise                |
| Limitation            | Not suitable for complex logic   |
"""