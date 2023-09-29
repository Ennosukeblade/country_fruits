import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class ProductManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 3:
            errors["name"] = "Product name should be at least 3 characters"
        if int(postData['price']) <= 0:
            errors["price"] = "Price should be more than zero"
        if len(postData['image']) < 1:
            errors["img"] = "Image is required"
        return errors


class CategoryManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['category']) < 2:
            errors["category"] = "Category name should be at least 2 characters"
        return errors


# Users
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Categories
class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

# Products

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    image = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        return self.name


# Orders
class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)
    user = models.ForeignKey(User, related_name="user",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Order_items join product to order
class ProductOrder(models.Model):
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=3)
    order = models.ForeignKey(
        Order, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="products", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Addresses
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    postal_code = models.PositiveIntegerField(null=True)
    phone = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name="address_user",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash_on_delivery', 'Cash on Delivery'),
        # Add more payment method choices as needed
    ]
    order = models.ForeignKey(
        Order, related_name="order", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
