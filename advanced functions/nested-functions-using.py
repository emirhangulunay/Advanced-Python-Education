# def outer(number):
#     def inner(number):
#         print(number)

#     inner(number)

# outer(10)

def factorial(sayi):
    if not isinstance(sayi, int):
        raise TypeError("number must be an int")

    if not sayi >= 0:
        raise ValueError("number must be zero or positive")
    
    def inner_factorial(sayi):
        if sayi <= 1:
            return 1
        return sayi * inner_factorial(sayi - 1)

    return inner_factorial(sayi)


sonuc = factorial(5)

try:
    sonuc = factorial(5)
    print(sonuc)
except Exception as ex:
    print(ex)

    
    