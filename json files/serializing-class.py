import json


class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

#serialize

# p1 = Product(1, "Samsung S26", 7000)
# p2 = Product(2, "Redmi S26", 5500)

# # products = [p1.__dict__, p2.__dict__]

# product = {
#     p1.id : p1.__dict__,
#     p2.id : p2.__dict__
# }

# with open("products.json", "w") as file:
#     json.dump(p1.__dict__, )

#deserialize

with open("products.json") as file:
    products = json.load(file)

urunler = []
print(type(products))
for key, value in products.items():
    urunler.append(Product(key, value["title"], value["price"]))

print(type(urunler))

for p in urunler:
    print(p.title)
