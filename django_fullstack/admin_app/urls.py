from django.urls import path
from . import views

urlpatterns = [
    path('new_product', views.new_product),
    path('addproduct', views.add_product, name="add_product"),
    path('', views.display_products),
    path('addcategory', views.add_category, name="add_category"),
    path('categories', views.display_categories),

]
