sayilar = [1,4,6,32,23,12]
harfler = ['a', 'c', 'v', 'z']
isimler = ['ahmet', 'ali', 'yiğit']


sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)
sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min([len(isim) for isim in isimler])
sonuc = max([len(isim) for isim in isimler])


sonuc = max(isimler, key = lambda isim: len(isim))
sonuc = min(isimler, key = lambda isim: len(isim))

urunler = [
    {"title": "samsung s23", "price":70000},
    {"title": "samsung s24", "price":80000},
    {"title": "samsung s25", "price":90000},
]

sonuc = min(urunler, key = lambda urun: urun["price"])
sonuc = max(urunler, key = lambda urun: urun["price"])["title"]

print(sonuc)["title"] #ya da değişkene yaz max(urunler, key = lambda urun: urun["price"])["title"]