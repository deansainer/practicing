from django.shortcuts import render
from .models import *


def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', context={'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', context={'products': products})


def product_details(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(request, 'myapp/product_details.html', context={'product': product})
