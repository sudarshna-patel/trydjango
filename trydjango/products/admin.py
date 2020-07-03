from django.contrib import admin

# Register your models here.

# it is called relative import
from .models import Product

admin.site.register(Product)