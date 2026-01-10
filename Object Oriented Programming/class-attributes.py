class CartItem:
    discount_rate = 0.8
    item_count = 0
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1

    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self, rate):
        self.price = self.price * rate

        
#instance => nesne, örnek
item1 = CartItem("Telefon", 5000,2)
item2 = CartItem("Bilgisayar", 6000,1)
item3 = CartItem("Kitap", 700 ,3)
item4 = CartItem("Televizyon", 3000 ,1)

print(item1.__dict__)
print(item2.__dict__)
print(item3.__dict__)
print(item4.__dict__)
print(CartItem.__dict__)

print(CartItem.item_count)

item1.apply_discount(0.8)
print(item1.calculate_total())

item2.apply_discount(0.7)
print(item2.calculate_total())

item3.apply_discount(0.9)
print(item3.calculate_total())
