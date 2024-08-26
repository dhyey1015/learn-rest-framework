import requests

# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"


get_response = requests.get(endpoint, json= {"xyz" : "hello world!"})
print(get_response.text)
print(get_response.status_code)

# print(get_response.json())