from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer




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