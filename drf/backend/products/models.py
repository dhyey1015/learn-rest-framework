from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    price = models.DecimalField(max_digits=15, decimal_places=2,default=99.99)
    
    @property
    def sale_price(self):
        sale_p = float(self.price)
        sale = (sale_p * 0.8)
        return f"{sale:.2f}"
    
    def discount_price(self):
        return "122"


        
    