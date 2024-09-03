import algoliasearch_django as algoliasearch # type: ignore

from .models import Product

algoliasearch.register(Product)