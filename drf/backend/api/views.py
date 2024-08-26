from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_home(request):
    
    print(request.GET)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type 
    data['params'] = dict(request.GET)
    return JsonResponse(data)

