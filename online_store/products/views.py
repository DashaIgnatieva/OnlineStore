from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "Магазин",
        "is_promotion": True
    }
    return render(request, 'products/index.html', context=context)

def products(request):
    context = {
        "title": "Магазин | Каталог",
        "products": [
            {
                "image":"static/vendor/img/products/product1_mice.jpg",
                "name":"Кормовые мыши",
                "prise":100,
                "description":"Кормовые мыши разных размеров."
            },
            {
                "image":"static/vendor/img/products/product1_mice.jpg",
                "name":"Кормовые мыши",
                "prise":100,
                "description":"Кормовые мыши разных размеров."
            },
            {
                "image":"static/vendor/img/products/product1_mice.jpg",
                "name":"Кормовые мыши",
                "prise":100,
                "description":"Кормовые мыши разных размеров."
            }
        ]
    }
    return render(request, 'products/products.html', context=context)