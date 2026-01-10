sayilar = [

]

for i in range(5):
    sayilar.append(i)


sayilar2 = [i for i in range(5)]

print(sayilar)
print(sayilar2)



kurum = "Btk Akademi"

for i in kurum:
    print(i.upper())


sonuc = [i.upper() for i in kurum]

print(sonuc)

