import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "emirhangulunay",
    database = "example"
)

cursor = db.cursor()
def updateProduct(id, name, price):
    sql = "UPDATE products SET name = %s, price=%s WHERE id = %s"
    params = (name, price, id)
    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as error:
        print(error)

    finally:
        db.close()
        cursor.close()

updateProduct(2, "Samsung S26-Updated",20000)