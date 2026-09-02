import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()

sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"

# value = ("Iphone 16", 70000, "3.jpg", "iyi bir telefon")
#cursor.execute(sql, value)
values = [
    ("Iphone 17", 764000, "3.jpg", "iyi bir telefon")
    ("Iphone 19", 706600, "3.jpg", "iyi telefon")
    ("Iphone 16", 7500, "3.jpg", "kötü telefon")
    ]

cursor.executemany(sql, values)

try:
    db.commit()
    print(cursor.rowcount, "kayıt edildi")
    print(f"son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as error:
    print("hata", error)

finally: 
    cursor.close()
    db.close()
    print("bağlantı kesildi")