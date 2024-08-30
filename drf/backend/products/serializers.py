from rest_framework import serializers
from rest_framework.reverse import  reverse 
from .validators import validate_title, validate_title_no_hello, unique_product_title

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only = True)
    url = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    #preffered method to to use urls in rest frame work
    preffered_url = serializers.HyperlinkedIdentityField(
        view_name= 'product_detail',
        lookup_field ='pk'
    )
    
    # email = serializers.EmailField(write_only = True)
    
    #second way to do validate the fields in serializer validate_title is comming from validators.py 
    title = serializers.CharField(validators=[unique_product_title, validate_title_no_hello])
    #name = serializers.CharField(source = 'title', read_only=True) we can use foregionkey too
     
    
    class Meta:
        model = Product
        fields = [
            # 'user',
            'preffered_url',
            'url',
            'edit_url',
            'pk',
            'title',
            # 'user',
            'content',
            'price',
            'sale_price',
            'discount',
            
        ]
    #one way to do validate the fields in serializer  we will use it here when we are using context.get 
     
    # def validate_title(self, value):
    #     request =  self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise   serializers.ValidationError(f"{value} is already product name")
    #     return value    
        
    
    # #to create model by overwriting the default method to create a model 
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance
    
    #one way to use reverse    
    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_detail",kwargs ={"pk": obj.pk}, request=request)
    
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_edit",kwargs ={"pk": obj.pk}, request=request)
    
    #another way to use reverse and its preffered 
    
    
    
        
    def get_discount(self, obj):
        try:
            return obj.discount_price()
        except:
            return None