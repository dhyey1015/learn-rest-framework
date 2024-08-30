from rest_framework import serializers
from rest_framework.reverse import  reverse 


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
    
    email = serializers.EmailField(write_only = True)

    
    class Meta:
        model = Product
        fields = [
            'preffered_url',
            'url',
            'edit_url',
            'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            
        ]
    #to create model by overwriting the default method to create a model 
    def create(self, validated_data):
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj)
        return obj
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        return instance
    
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