####for generic rest framework(list)############

import requests
from getpass import getpass

# GET AUTH RESPONSE (TOKEN AUTHENTICATION)
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("what is your user name? ")
password = getpass("what is your password? ")
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})

try:
    print(auth_response.json())
except:
     print("The response is not in JSON format.")
     exit()
     
     
     
#GET RESPONSE      
if auth_response.status_code == 200:    
   
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    #endpoint = "http://localhost:8000/api/products/mixins/"

    get_response = requests.get(endpoint, headers=headers)

    try:
        data = get_response.json()
        next_url = data["next"]
        results = data['results']
        print("next_url", next_url)
        print(results)
    except:
        print("The response is not in JSON format.")