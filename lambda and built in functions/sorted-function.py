sayilar = [1,5,4,67,8,9]

#sayilar.sort()

sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)

users = [
    {"username":"sadikturan", "posts": ["post 1", "post 2"], "email" : "info@abc.com", 
     "phone": "123123"
     },
    {"username":"ahmet", "posts": ["post 1"], "email" : "info@abc.com"},
    {"username":"canan", "posts": ["post 1", "post 2","post3"]},

]



sonuc = sorted(users, key = len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda user: len(user["posts"]))

sonuc = list(map
             (
                 lambda user: user["username"], 
                 sorted(
                     users, key=lambda user: len(user["posts"])
                        )))


kurslar = [
    {"title": "python", "count": 1000},
    {"title": "web", "count": 2000},
    {"title": "javascript", "count": 3000}
]

sonuc = sorted(kurslar, key = lambda kurs: kurs["count"])
sonuc = sorted(kurslar, key = lambda kurs: kurs["count"], reverse=True)
sonuc = list(map(lambda kurs: kurs["title"], sorted(kurslar, key = lambda kurs: kurs["count"], reverse=True)))


print(sonuc)
