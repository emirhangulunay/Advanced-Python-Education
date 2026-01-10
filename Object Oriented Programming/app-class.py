import random as rd

class CartItem:
    discount_rate = 0.8
    item_count = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    @classmethod 
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))
    
    def apply_discount(self):
        self.price *= CartItem.discount_rate

    def calculate_total(self):
        return self.price * self.quantity

class ShoppingCart:
    coupon_dict = {}

    @classmethod
    def get_coupons(cls):
        coupon_name = f"coupon{len(cls.coupon_dict)+1}"

        make_coupon_elements = [
            x
            for letter in [rd.choice(list('abcdefghijkl'))]
            for x in [letter] + [rd.randrange(101) for _ in range(3)]
        ]
        created_coupon = ''.join(str(x) for x in make_coupon_elements)

        cls.coupon_dict[coupon_name] = created_coupon
        print(cls.coupon_dict)

    @classmethod
    def get_coupon(cls, coupon_name):
        if coupon_name in cls.coupon_dict:
            print(f"""
            {coupon_name} adında bir kupon bulunuyor. İşte bilgiler: 
            Kupon adı: {coupon_name}, kodu: {cls.coupon_dict[coupon_name]}
            Kopyalamak için seçiniz ▽ 
            {cls.coupon_dict[coupon_name]}
            """)
        else:
            print("Kupon adı yanlış")
    
    def __init__(self, items=None):
        self.items = items if items else []

    def apply_coupon(self, coupon_name):
        if coupon_name in self.coupon_dict:
            for item in self.items:
                item.apply_discount()
            print(f"{coupon_name} kuponu uygulandı. İndirim yapıldı!")
        else:
            print("Kupon adı yanlış")

    def add_item(self, *items):
        self.items.extend(items)
        print("Ürün eklendi!")

    def display_items(self):
        if not self.items:
            print("Sepet boş.")
            return
        for x in self.items:
            print(f"Bütün alınanlar: {x.__dict__}")

    def calculate_totals(self):
        total = sum(item.calculate_total() for item in self.items)
        print(f"Toplam tutar: {total}")
        return total

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} kaldırıldı.")
        else:
            print(f"{item.name} sepetinizde yok.")

    def clear(self):
        self.items.clear()
        print("Ürünler silindi.")

item1 = CartItem("Telefon", 5000, 2)
item2 = CartItem("Bilgisayar", 6000, 1)
item3 = CartItem("Kitap", 700, 3)

sc = ShoppingCart([item1, item2])

sc.add_item(item3)
sc.display_items()

sc.calculate_totals()

sc.remove_item(item1)
sc.display_items()

sc.clear()
sc.display_items()

ShoppingCart.get_coupons()
ShoppingCart.get_coupon("coupon1")  
