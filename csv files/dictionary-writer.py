import csv

# with open("products-2-.csv", "w", newline='') as file:
#     headers = ["Id", "ProductName", "Price", "IsActive","Category","Rating"]
#     csv_writer = csv.DictWriter(file, headers)
#     csv_writer.writeheader()
    # csv_writer.writerow({
    #     "ProductName":"Iphone 14",
    #     "Price" : 4000,
    #     "IsActive" : True,
    #     "Category" : "Telefon",
    #     "Rating" : 4.6

    # })
    # csv_writer.writerow({
    #         "ProductName":"Iphone 16",
    #         "Price" : 4000,
    #         "IsActive" : True,
    #         "Category" : "Telefon",
    #         "Rating" : 4.6

    #     })
    # csv_writer.writerow({
    #         "ProductName":"Iphone 17",
    #         "Price" : 4000,
    #         "IsActive" : True,
    #         "Category" : "Telefon",
    #         "Rating" : 4.6

    #     })

    # csv_writer.writerows([
    #     {
    #         "ProductName":"Iphone 17",
    #         "Price" : 4000,
    #         "IsActive" : True,
    #         "Category" : "Telefon",
    #         "Rating" : 4.6
    #     },
    #             {
    #         "ProductName":"Iphone 17",
    #         "Price" : 4000,
    #         "IsActive" : True,
    #         "Category" : "Telefon",
    #         "Rating" : 4.6
    #     },
    #             {
    #         "ProductName":"Iphone 17",
    #         "Price" : 4000,
    #         "IsActive" : True,
    #         "Category" : "Telefon",
    #         "Rating" : 4.6
    #     }
    # ])




# with open("products-2.csv", "a", newline='') as file:
#     headers = ["Id", "ProductName", "Price", "IsActive","Category","Rating"]
#     csv_writer = csv.DictWriter(file, headers)
#     csv_writer.writeheader()
#     csv_writer.writerow(
#         {
#             "Id" : 4,
#             "ProductName":"Iphone 17",
#             "Price" : 4000,
#             "IsActive" : True,
#             "Category" : "Telefon",
#             "Rating" : 4.6
#         })


def price_tax(price):
    return price * 2

with open("products-2.csv") as file:
    csv_reader = csv.DictReader(file)
    products = list(csv_reader)

    with open("products-3.csv", "w", newline='') as file:
        headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
        csv_writer = csv.DictWriter(file, headers)
        csv_writer.writeheader()

        for u in products:
            csv_writer.writerow({
            "Id" : u["Id"],
            "ProductName" : u["ProductName"],
            "Price" : price_tax(u["Price"]),
            "IsActive" : u["IsActive"],
            "Category" : u["Category"],
            "Rating" : u["Rating"]
            })






