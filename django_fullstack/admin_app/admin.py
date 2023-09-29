from django.contrib import admin

# Register your models here.
from .models import Product, Category, Order, User

admin.site.register([Product, Category, Order, User])
