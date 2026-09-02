import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
sql = "SELECT id, name FROM products"

cursor.execute(sql)

products = cursor.fetchall()

print(products)

# for i in products:
#     print(i[0, i[1]])