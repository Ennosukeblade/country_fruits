from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView, Response

from admin_app.models import Product
from .serializers import ProductOrderSerializer, ProductSerializer

# Create your views here.

# def get_all_products(request):
#     query = Product.objects.all()
#     data = serializers.serialize("json", query)
#     print('HTTP---',data)
#     return HttpResponse(data)


class ProductsListApiView(APIView):
    def get(self, request):
        # id = request.query_params['id']
        products = Product.objects.all()
        print('QUERY-------', products.values())
        # data = serializers.serialize("json", query)
        serialized_data = ProductSerializer(products, many=True)
        print('DATA-------', serialized_data.data)
        # response_data = {"data":data}
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class ProductDetailApiView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        # serialized_data={
        #     'id': data.id,
        #     'name': data.name,
        #     'price': data.price,
        #     'quantity': data.quantity,
        #     'description': data.description,
        #     'image': data.image,
        #     'category_id': data.category_id,
        #     'created_at': data.created_at,
        #     'updated_at': data.updated_at,
        # }
        serialized_data = ProductSerializer(product)
        print("MY PRODUCT------", serialized_data.data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    # def create(self, request):

    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        """
        Create a new product order.
        """
        print("REQ DATA------", request.data)
        request.data["product"] = id
        print("REQ DATA------", request.data)
        serializer = ProductOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
