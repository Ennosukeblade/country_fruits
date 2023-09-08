from rest_framework import serializers

from admin_app.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name",
                  "price",
                  "quantity",
                  "description",
                  "image",
                  "category",
                  "created_at",
                  "updated_at"]