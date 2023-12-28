from django.contrib import admin

from products.models import ProductCategory, Product

# Регистрация моделей нужна для их отображения в админке
admin.site.register(Product)
admin.site.register(ProductCategory)

