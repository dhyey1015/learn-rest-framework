from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404



#if we use generic views(mentos life)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #or we can product_detial_view = ProductDetailAPIView.as_view()
    

class ProductListAPIView(generics.ListAPIView): 
    """_
    no going to use it cause we can make list and create togather
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#if we don't use generic views  (normal life)
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        #detail view
        if pk is not None:
            # queryset = Product.objects.filter(pk=pk) one way to do it 
            # if not queryset.exists():
            #     raise Http404
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
            
        #listview    
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == 'POST':
        #create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')or None
            if content is None:
                content = title
            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status= 404)
        