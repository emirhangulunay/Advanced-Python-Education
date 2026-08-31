import requests 

response = requests.ger("https://jsonplaceholder.typicode.com/posts", data={
    "userId": 1,
    "title": "yeni gönderi",
    "body": "yeni gönderi açıklaması"

})


result = response
result = response.text
result = response.json()
result = response.headers




print(result)



