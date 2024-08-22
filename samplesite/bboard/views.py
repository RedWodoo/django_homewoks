from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'bboard/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'bboard/add_product.html', {'form': form})

class ProductListView(ListView):
    model = Product
    template_name = 'bboard/product_list.html'
    context_object_name = 'products'