from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    will do:
    get -> list -> Queryset
    get -> retrieve -> Product Instance/Detail view
    post -> create -> new instance
    put -> Update
    patch -> Partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk' #default
    
    
class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
    will do:
    get -> list -> Queryset
    get -> retrieve -> Product Instance/Detail view
    
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk' #default
    
#product_view_list = ProductGenericViewSet.as_view({'get':'list'}) #<----------------declare this if you want your viewsets to be displayed on urls
#product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
    