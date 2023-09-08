from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView,Response

from admin_app.models import Product
from .serializers import ProductSerializer

# Create your views here.

# def get_all_products(request):
#     query = Product.objects.all()
#     data = serializers.serialize("json", query)
#     print('HTTP---',data)
#     return HttpResponse(data)

class ProductsListApiView(APIView):
    
    # def get(self,request):
    #     query = Product.objects.all()
    #     data = serializers.serialize("json", query)
    #     print('DATA-------',data)
    #     response_data = {"data":data}
    #     return Response(response_data,status=status.HTTP_200_OK)
    # def get(self,request):
    #     items = [
    #         "apple",
    #         "mango",
    #         "grapes"
    #     ]
    #     response_data = {"datas":items}
    #     return Response(response_data,status=status.HTTP_200_OK)
    def get(self, request):
        #id = request.query_params['id']
        products = Product.objects.all()
        print('QUERY-------',products.values())
        # data = serializers.serialize("json", query)
        serialized_data = ProductSerializer(products, many=True)
        print('DATA-------',serialized_data.data)
        # response_data = {"data":data}
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    
class ProductDetailApiView(APIView):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        serialized_data={
            'id': data.id,
            'name': data.name,
            'price': data.price,
            'quantity': data.quantity,
            'description': data.description,
            'image': data.image,
            'category_id': data.category_id,
            'created_at': data.created_at,
            'updated_at': data.updated_at,
            
        }
        return Response(serialized_data, status=status.HTTP_200_OK)