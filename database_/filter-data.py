import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()


# sql = "SELECT * FROM products WHERE id = 1"
# sql = "SELECT * FROM products WHERE id >= 1"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25'"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25' and price = 50000"
# sql = "SELECT * FROM products WHERE name = 'Samsung S25' or price = 50000"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung%'"
# sql = "SELECT * FROM products WHERE name LIKE 'Samsung%'"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung'"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung' or description LIKE '%iyi%'"



# result = cursor.fetchone()




def getProductById(id):
    sql = "SELECT * FROM products WHERE id = %"
    params = (id, )
    cursor.execute(sql, params)
    result = cursor.fetchall()
    print(result)

getProductById(1)