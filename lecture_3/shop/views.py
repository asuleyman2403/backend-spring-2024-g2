from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm


def index_page(request):
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


def products_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})


def delete_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/')
    except Product.DoesNotExist as e:
        form = CreateProductForm()
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products,
                                                   'form': form,
                                                   'error': 'Could delete product since it does not exist'
                                                   })


