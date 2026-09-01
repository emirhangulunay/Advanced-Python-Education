import requests

url = "http://api.openweathermap.org/geo/1.0/current.json"
key = "*"

konum = input("konum: ")

response = requests.get(url, params={
    "key" : key,
    "q" : konum,
    "lang" : "tr"
})

result = response.json()
city = result["location"]["name"]
weather = result["current"]["temp_c"]
text = result["current"]["condition"]["text"]

print(f"{city} şu anda {weather} derece ve {text}")