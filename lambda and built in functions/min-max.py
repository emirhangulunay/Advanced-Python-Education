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
sonuc = max(urunler, key = lambda urun: urun["price"])
print(sonuc["title"])


"""
| Topic            | Description                             |
| ---------------- | --------------------------------------- |
| Purpose          | Find the smallest or largest element    |
| Basic Usage      | `min(iterable)`, `max(iterable)`        |
| Numbers          | Compared by numeric value               |
| Strings          | Compared alphabetically (Unicode order) |
| Default Return   | Returns the original element            |
| `key` Parameter  | Defines the comparison rule             |
| `key` Example    | `key=lambda x: len(x)`                  |
| Dictionary Lists | Often used with `key`                   |
| Common Case      | Finding min/max by price, length, score |
| Important Note   | `print()` returns `None`                |
"""