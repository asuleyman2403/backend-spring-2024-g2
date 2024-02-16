from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import CategoryProductForm, ProductForm, CategoryForm
from django.contrib import messages


def index_page_view(request):
    categories = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(name=form.data.get('name'))
            category.save()
        return render(request, 'shop/index.html', {'categories': categories, 'form': form})
    return render(request, 'shop/index.html', {'categories': categories, 'form': form})


def category_page_view(request, pk):
    if request.method == 'GET':
        category = Category.objects.get(id=pk)
        products = Product.objects.filter(category_id=category.id)
        form = CategoryProductForm()
        return render(request, 'shop/category.html', {'category': category, 'products': products, 'form': form})
    if request.method == 'POST':
        category = Category.objects.get(id=pk)
        products = Product.objects.filter(category_id=category.id)
        form = CategoryProductForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            price = form.data.get('price')
            amount = form.data.get('amount')
            description = form.data.get('description')
            product = Product(name=name, price=price, amount=amount, description=description, category_id=category.id)
            product.save()
            products = Product.objects.filter(category_id=category.id)
            form = CategoryProductForm()
            return render(request, 'shop/category.html', {'category': category, 'products': products, 'form': form})
        return render(request, 'shop/category.html', {'category': category, 'products': products, 'form': form})


def edit_product_page_view(request, pk):
    product = Product.objects.get(id=pk)
    categories = Category.objects.all()
    if request.method == 'GET':
        form = ProductForm(data={'name': product.name, 'price': product.price, 'amount': product.amount,
                                 'description': product.description, 'category': product.category.id})
        return render(request, 'shop/edit-product.html', {'product': product, 'form': form, 'categories': categories})
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.data.get('name', product.name)
            product.price = form.data.get('price', product.price)
            product.amount = form.data.get('amount', product.amount)
            product.description = form.data.get('description', product.description)
            product.category_id = form.data.get('category', product.category.id)
            product.save()
            return redirect(to='products_page')
        else:
            form = ProductForm(data={'name': product.name, 'price': product.price, 'amount': product.amount,
                                     'description': product.description, 'category': product.category.id})
            return render(request, 'shop/edit-product.html', {'product': product, 'form': form, 'categories': categories})


def products_page_view(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        form = ProductForm()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products, 'form': form, 'categories': categories})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            price = form.data.get('price')
            amount = form.data.get('amount')
            description = form.data.get('description')
            category_id = form.data.get('category')
            product = Product(name=name, price=price, amount=amount, description=description, category_id=category_id)
            product.save()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products, 'form': form, 'categories': categories})


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
