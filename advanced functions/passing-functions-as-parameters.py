def filter(fn, liste):
    result = []
    for item in liste:
        if fn(item):
            result.append(item)

    return result

def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0 


sayilar = [1,2,3,4,5,6,7,8,9]

sonuc = filter(is_even, sayilar)
sonuc = filter(is_positive, sayilar)
