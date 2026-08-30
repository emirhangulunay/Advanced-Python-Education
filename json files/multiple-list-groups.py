import json

db = {
    "users" : {
        "emirhangulunay": 
        {"firstname" : "Emirhan",
        "lastname" : "Gulunay"},
        "aligulunay": 
        {"firstname" : "Ali",
        "lastname" : "Gulunay"
        },
        },
    "products": {
        "1": {
        "title": "Macbook Pro",
        "price": 80000
        },

        "2" : {
        "title": "Macbook Air",
        "price": 70000
        },

        "3": {
        "title": "Iphone 17 Pro Max",
        "price": 120000
        }
    }
}

# with open("db.json", "w", encoding="utf-8") as file:
#     json.dump(db, file, ensure_ascii=False, indent=2)

with open("db.json") as file:
    data = json.load(file)

print(data["users"]["emirhangulunay"])
print(data["products"]["2"]["price"])

data["products"].update({
            "3": {
        "title": "Iphone 17 Pro Max",
        "price": 120000
        }
})


with open("db.json", "w", encoding="utf-8") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)