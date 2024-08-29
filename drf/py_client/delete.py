####for generic rest framework(detail)############
import requests
headers = {'Authorization': 'Bearer c4ed6c994b6eb7d25bd810d07d6de23937ca35de'}

product_id = input("choose a product id you want to delete? ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")
    
if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint, headers=headers)

    try:
        print(get_response.status_code, get_response.status_code == 204)
    except:
        print("The response is not in JSON format.")
        
        
        
        
        
        
        
        
        
#, json= {"title" : "hello hello world!", "content" : "hello", "price": "12"}

# data = {
#     "title" : "hello hello hello hello world!",
#     "price": 122222222222
# }