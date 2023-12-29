from django.shortcuts import render

from products.models import ProductCategory, Product

def index(request):
    context = {
        "title": "Магазин",
        "is_promotion": True
    }
    return render(request, 'products/index.html', context=context)

def products(request):
    context = {
        "title": "Магазин | Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context=context)