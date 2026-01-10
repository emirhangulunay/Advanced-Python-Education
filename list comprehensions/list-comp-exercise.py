#1
first_answer = [x for x in range(101) if x % 12 == 0]

#2

text = "Hello 12345 World"

second_answer = [x for x in text if x.isdigit()]

#3

sicakliklar = [20,15,0,-5,-2]

third_answer = [x  if x >= 4 else "Buzlanma tehlikesi" for x in sicakliklar]


#4

ogrenciler = ["ali", "ahmet", "canan"]
notlar = [50,60,80]

#[("ali", 50), ("ahmet", 60), ("canan", 80)]

liste = [(ogrenciler[i], notlar[i]) for i in range(0, len(ogrenciler))]
liste_dict = {key:value for (key, value) in liste if value > 50}



#5

sonuc = []

for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

print(sonuc)



list = [(i, j) for i in range(3) for j in range(3)]

print(list)
