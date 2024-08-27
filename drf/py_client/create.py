####for generic rest framework(create)############

import requests

# endpoint = "http://localhost:8000/api/products/create/"
endpoint = "http://localhost:8000/api/products/list_mixins/"

#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}
data = {
    "title" : "hello hello world! hello hello",
    "price": "12"
}
get_response = requests.post(endpoint, json = {
    "title" : "hello hello world!",
    "price": "1222222222222"
})


try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")