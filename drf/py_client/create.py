####for generic rest framework(create)############

import requests

endpoint = "http://localhost:8000/api/products/1/"

#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}
get_response = requests.get(endpoint)

try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")