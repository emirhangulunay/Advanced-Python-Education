from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

obj =  BeautifulSoup(html, "html.parser")

result = obj.div
result = obj.div("div")
result = obj.div(id="item1")
result = obj.div(id="item2")
result = obj.div(id="header")
result = obj.div(class_="item")
result = obj.div(class_="item")[1]

result = obj.select("#header")
result = obj.select("#item1")
result = obj.select(".item1")
result = obj.select_one(".item")
result = obj.attrs["class"]
result = obj.attrs["id"]

result = obj.ul.get_text(strip=True, seperator="-")

for a in obj.div.find_all("a"):
    print(a["href"])

print(result)