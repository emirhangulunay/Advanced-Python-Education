import json

data = [
    {
        "id": 1,
        "title": "Macbook Pro",
        "price": 80000
    },
    {
        "id": 1,
        "title": "Macbook Pro",
        "price": 80000
    }
]


with open("products.json") as file:
    products = json.load(file)

print(products[2])
print(products[3])

products.update({
    "1" : {
        "title" : "Macbook Pro",
        "price" : 80000
    }
})


with open("products.json", "w", encoding= "utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)