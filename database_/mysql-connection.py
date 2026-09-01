import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()

# cursor.execute("Create Database example database")
# cursor.execute("Shown Databases")


cursor.execute("CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) )")

cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)