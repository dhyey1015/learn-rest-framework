from rest_framework import serializers



class UserProductInlineSerializer(serializers.Serializer): #this serializer will serialize the my_products_qs data
    preffered_url = serializers.HyperlinkedIdentityField(
            view_name= 'product_detail',
            lookup_field ='pk',
            read_only = True
        ) #to make hyper link work bring context = {'request':request}
    title = serializers.CharField(read_only= True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True) #<--- this is practical for everywhere 
    id = serializers.IntegerField(read_only = True)#<--- this is practical for everywhere 
    # other_products = serializers.SerializerMethodField(read_only = True)

    # def get_other_products(self, obj):
    #     print(obj)                                            ###only for learning purpose that we can show nested data too if we wnat####
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs, many = True, context = self.context).data#<------------ idk what many is here find out!!