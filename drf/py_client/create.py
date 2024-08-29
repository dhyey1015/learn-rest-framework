####for generic rest framework(create)############

import requests
headers = {'Authorization': 'Bearer c4ed6c994b6eb7d25bd810d07d6de23937ca35de'}
endpoint = "http://localhost:8000/api/products/create/"
#endpoint = "http://localhost:8000/api/products/mixins/"

#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}
data = {
    "title" : "hello hello world! hello hello",
    "price": "12"
}
get_response = requests.post(endpoint, json = {
    "title" : "hello hello world!",
    "price": "1222222222222"
}, headers=headers)


try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")