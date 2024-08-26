####for generic rest framework(detail)############

import requests

endpoint = "http://localhost:8000/api/products/"

#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}

data = {
    "title" : "hello hello world!",
    "price": "12"
}
get_response = requests.post(endpoint, json = data)

try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")