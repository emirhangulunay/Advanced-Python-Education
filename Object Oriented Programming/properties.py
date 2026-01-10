class Product: 
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
    
    @property
    def price(self):
        return self._price 

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else: 
            raise ValueError("ürün fiyatı için negatif değer ataması  yapılmaz")
        


p = Product("Iph 16", 80000)

print(p.price)
p.price = 90000
print(p.price)