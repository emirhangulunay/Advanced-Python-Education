sayilar = [1,3,5,4,32,56]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 15)

products = [
    {"title": "samsung s23", "price":70000},
    {"title": "samsung s24", "price":80000},
    {"title": "samsung s25", "price":90000},
]

toplamFiyat = sum([urun["price"] for urun in products])
urunAdeti = len([urun for urun in products if urun["price"]> 0]) 
sonuc = toplamFiyat / urunAdeti

sonuc = round(5.3)
sonuc = round(5.6)
sonuc = round(5.5)
sonuc = round(1.3263534, 2)
sonuc = round(1.3263534, 4)
