import csv

# with open("cars.csv", "w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Marka", "Model"])
#     csv_writer.writerow(["Toyota", "Corolla"])
#     csv_writer.writerow(["Mazda", "CX-5"])
#     csv_writer.writerows([["Marka", "Model"],["Toyota", "Corolla"],["Toyota", "Yaris"]])


# with open("cars.csv", "a") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Mazda", "CX-5"])


# with open("products.csv") as file:
#     csv_reader = csv.reader(file)
#     with open("products.csv", "w", newline='') as f:
#         csv_writer = csv.writer(f)
#         for urun in csv_reader:
#             csv_writer.writerow([u.upper() for u in urun])





with open("products.csv", "r+", newline='') as file:
    csv_reader = csv.reader(file)
    csv_writer = csv.writer(file)

    next(csv_reader)
    products = [[u[0],u[1],float(u[2])*1.2,u[3],u[4],u[5]] for u in csv_reader]

    file.seek(0)

    csv_writer.writerow(["ID","ProductName","Price","IsActive","Category","Rating"])
    csv_writer.writerows(products)



