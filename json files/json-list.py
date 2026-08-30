import json

data = [
    {
    "id" : 1,
    "title": "Macbook Pro",
    "price": 80000
    },
    {
        "id": 2,
        "title": "Macbook Air",
        "price": 70000
    }
]

product = {
        "id": 2,
        "title": "Iphone 17 Pro Max",
        "price": 118999
}

with open("products.json") as file:
    products = json.load(file)


for p in products:
     if p["title"] == "Iphone 17 Pro Max":
        p["price"] = 120000


products.remove(products[0])
# products.append(product)

with open("products.json", "w", encoding="utf-8") as file:
     json.dump(products, file, ensure_ascii=False, indent=2)



