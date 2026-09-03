import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()

# sql = "SELECT name, categoryid FROM categories"
# sql = "SELECT name FROM categories"
sql = "SELECT * from products inner join categories on products inner join categories on products.categoryid=categories.id"