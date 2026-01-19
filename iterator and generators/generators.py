def counter(max):
    sayi = 1
    sayilar = [

    ]
    while sayi <= max:
        yield sayi
        sayi += 1

    
    return sayilar

generator = counter(20)

# print(generator)
# print(dir(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)


sonuc = list(generator)

liste = (i for i in range(1,20))
print(next(liste))