import requests

# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, params={"abc" : 123}, json= {"query" : "hello world!"})
#print(get_response.text)
#print(get_response.status_code)
try:
    print(get_response.json())
except:
     print("The response is not in JSON format.")