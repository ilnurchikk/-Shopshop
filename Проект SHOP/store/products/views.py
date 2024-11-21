from django.shortcuts import render

from products.models import ProductCategory, Product
def index(request):
    context = {
        'title': 'Store',
        'sale': 'Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'is_sale': False,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)