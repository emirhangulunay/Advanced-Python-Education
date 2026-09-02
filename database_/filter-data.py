import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()


sql = "SELECT * FROM products WHERE id = 1"

result = cursor.fetchone()

print(result)