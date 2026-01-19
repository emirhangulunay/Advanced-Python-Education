sayilar = iter([i for i in range(0,7)])

while True:
    try:
        sayi = next(sayilar)
        print(sayi)

    except StopIteration:
        break


# print(next(iterator))
# s = "BTK Akademi"
# a = 10

# for i in a:
#     print(i)