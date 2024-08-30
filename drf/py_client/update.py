####for generic rest framework(detail)############

import requests
headers = {'Authorization': 'Bearer c4ed6c994b6eb7d25bd810d07d6de23937ca35de'}

endpoint = "http://localhost:8000/api/products/1/update/"

#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}

data = {
    "title" : "hello hello hello hello world!",
    "price": 122222222222
}
get_response = requests.put(endpoint, json=data, headers=headers)

try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")