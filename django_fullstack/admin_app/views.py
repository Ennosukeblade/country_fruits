from django.shortcuts import redirect, render

from admin_app.models import Category, Product
from django.contrib import messages
import uuid
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp']

# Create your views here.

# * Add product display


def new_product(request):
    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})

# * Add product action


def add_product(request):

    print("*** image SUBMIT ***", request.FILES)

    image = ""
    if len(request.FILES) > 0:
        image = request.FILES['image']

    data = {
        'name': request.POST['name'],
        'description': request.POST['description'],
        'price': request.POST['price'],
        'category': request.POST['category'],
        'quantity': request.POST['quantity'],
        'image': image
    }

    errors = Product.objects.basic_validator(data)
    if data['image'] != "":
        if not accepted_extention(data['image']._name):
            errors["extention"] = "You have to upload a valid image or a gif"
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/cf-admin/new_product')

    image_name = handle_uploaded_file(request.FILES['image'])
    chosen_category = Category.objects.get(id=data['category'])
    Product.objects.create(name=data['name'],
                           price=data['price'],
                           image=image_name,
                           description=data['description'],
                           category=chosen_category,
                           quantity=data['quantity']
                           )
    return redirect('/cf-admin')


def handle_uploaded_file(f):
    print('*** FileName from ***', f)
    extension = f._name.rsplit('.', 1)[1]
    print("*** EXTENSION ***", extension)
    new_image_name = f"image-{uuid.uuid4()}.{extension}"
    with open(f"admin_app/static/img/{new_image_name}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return new_image_name


def accepted_extention(f):
    print(f)
    extension = f.rsplit('.', 1)[1]
    if extension.lower() in ALLOWED_EXTENSIONS:
        return True
    return False

# * Display Products


def display_products(request):
    products = Product.objects.all()
    one_product = Product.objects.get(id=1)
    print(one_product.category.name)
    return render(request, 'products.html', {'products': products})

# * Category


def display_categories(request):
    categories = Category.objects.all()
    return render(request, 'add_category.html', {'categories': categories})


def add_category(request):
    errors = Category.objects.basic_validator(
        {'category': request.POST['category']})
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/cf-admin/categories')
    Category.objects.create(name=request.POST['category'])
    return redirect('/cf-admin/categories')
