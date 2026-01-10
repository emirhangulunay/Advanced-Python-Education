class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

item1 = CartItem("Telefon", 5000,2)
item2 = CartItem("Bilgisayar", 6000,1)
item3 = CartItem("Kitap", 700 ,3)