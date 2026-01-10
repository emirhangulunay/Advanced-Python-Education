class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self, rate):
        self.price = self.price * CartItem.discount_rate

        
#instance => nesne, örnek
item1 = CartItem("Telefon", 5000,2)
item2 = CartItem("Bilgisayar", 6000,1)
item3 = CartItem("Kitap", 700 ,3)

item1.apply_discount()
print(item1.calculate_total())

item2.apply_discount()
print(item2.apply_discount())

item3.apply_discount()
print(item3.calculate_total())
