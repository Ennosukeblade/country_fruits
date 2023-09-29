from rest_framework import serializers

from admin_app.models import Product, ProductOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "quantity",
            "description",
            "image",
            "category",
            "created_at",
            "updated_at"]


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            "quantity",
            "subtotal",
            "order",
            "product"
        ]
