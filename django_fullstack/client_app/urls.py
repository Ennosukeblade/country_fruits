from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductsListApiView.as_view()),
    path('store/<int:id>/', views.ProductDetailApiView.as_view())
    # path('store', views.get_all_products)
]
