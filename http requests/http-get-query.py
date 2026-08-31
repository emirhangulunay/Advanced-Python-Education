import requests 

response = requests.ger("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true", params={
    "userId" : "1",
    "completed": "true"
})

todos = response.json()

sonuc = todos

# print(sonuc[0])
print(sonuc)



