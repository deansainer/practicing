from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *
from .forms import *


def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', context={'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', context={'products': products})


def product_details(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(request, 'myapp/product_details.html', context={'product': product})


class NewProductView(TemplateView):
    template_name = 'myapp/new_product.html'

    def get(self, request):
        form = NewProductForm
        return render(request, self.template_name, {'form': form})




