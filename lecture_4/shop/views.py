from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm
from django.contrib import messages


def index_page_view(request):
    return (to='products_page')


def products_page_view(request):
    if request.method == 'GET':
        form = CreateProductForm()
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products, 'form': form})
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            price = form.data.get('price')
            amount = form.data.get('amount')
            description = form.data.get('description')
            product = Product(name=name, price=price, amount=amount, description=description)
            product.save()
            products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products, 'form': form})


def product_details_page_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product-details.html', {'product': product})


def delete_product_page_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect(to='products_page')
    except Product.DoesNotExist as e:
        messages.error(request, 'Could delete product since it does not exist')
        return redirect(to='products_page')
