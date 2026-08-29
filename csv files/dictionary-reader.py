import csv

with open("products.csv") as file:
    csv_reader = csv.DictReader(file, delimiter="|")
    csv_reader = csv.DictReader(file)

    for i in csv_reader:
        if i["Category"] == "Telefon" and float(i["Category"]) >= 4.5:
            print(i["ProductName"], i["Price"])