from django.conf import settings
from django.db import models
from django.db.models import Q



class ProductQueryset(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user =None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQueryset(self.model, using = self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query, user = user)
        

# Create your models here.
User = settings.AUTH_USER_MODEL #auth.User
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=99.99)
    public = models.BooleanField(default= True)#<------Normally false
    
    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"
    
    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}/"

    @property
    def body(self):
        return self.content

    @property
    def sale_price(self):
        sale_p = float(self.price) 
        sale = (sale_p * 0.8)
        return f"{sale:.2f}"
    
    def discount_price(self):
        return "122"


        
    