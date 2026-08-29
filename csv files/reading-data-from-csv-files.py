import csv

with open("urunler.csv") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    # print(list(csv_reader))
    # liste = list(csv_reader)
    # print(liste[1])
    next(csv_reader)
    for i in csv_reader:
        if i[3] == "True":
            # print(i[0], i[1])
            print(f"ID: {i[0]}, Ad: {i[1]}")

        



