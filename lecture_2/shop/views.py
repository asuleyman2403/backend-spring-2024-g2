from django.shortcuts import render
from .models import Product


def index_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def products_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})



