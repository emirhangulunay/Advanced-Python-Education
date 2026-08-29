import csv

# with open("onlinefoods.csv") as file:
#     csv_reader = csv.reader(file)
#     liste = list(csv_reader)
#     print(len(liste) - 1)


# with open("onlinefoods.csv") as file:
#     csv_reader = csv.DictReader(file)
#     piece = len([user for user in csv_reader if user["Occupation"] == "Student"])
#     print(piece)



with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    users = [user for user in csv_reader if int(user["Age"]) > 20]
    for i in users:
        print(i["latitude"], i["longitude"])


