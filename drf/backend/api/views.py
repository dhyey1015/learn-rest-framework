from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
from products.models import *
import json
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

################ rest framework ######################

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def api_home(request):
    """
    DRF api view
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields= ['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
        
        return Response(data)
    # return HttpResponse(data, headers = {"Content-Type" : "application/json"})

