import requests

# endpoint = "https://httpbin.org"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json= {"title" : "hello hello world!"})

try:
    print(get_response.json())
    # print(get_response.headers)
    # print(get_response.text)
    #print(get_response.status_code)
    
except:
     print("The response is not in JSON format.")