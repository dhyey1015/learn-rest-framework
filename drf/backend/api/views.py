from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(request):
    
    return JsonResponse({"message" : "hi this the django api response"})

