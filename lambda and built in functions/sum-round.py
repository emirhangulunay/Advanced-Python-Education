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

"""
| Function                              | What it does               | Example result |
| ------------------------------------- | -------------------------- | -------------- |
| `sum(numbers)`                        | Adds all numbers           | `101`          |
| `sum(numbers, 15)`                    | Starts sum from 15         | `116`          |
| `sum([p["price"] for p in products])` | Sums product prices        | `240000`       |
| `len(list)`                           | Counts elements            | `3`            |
| `sum / len`                           | Calculates average         | `80000`        |
| `round(5.3)`                          | Rounds to nearest integer  | `5`            |
| `round(5.6)`                          | Rounds to nearest integer  | `6`            |
| `round(5.5)`                          | Bankers rounding (to even) | `6`            |
| `round(x, 2)`                         | Rounds to 2 decimals       | `1.33`         |
| `round(x, 4)`                         | Rounds to 4 decimals       | `1.3264`       |
"""