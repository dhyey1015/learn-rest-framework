from algoliasearch_django import AlgoliaIndex # type: ignore
from algoliasearch_django.decorators import register 

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    models = Product
    fields = {
        'title',
        'content',
        'price',
        'user',
        'public',
    }