from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *

def home(request):
    product = Product.objects.filter(is_available=True)
    category = Category.objects.all()
    context = {
        'title': 'Temny® Official Website',
        'product': product,
        'category': category,
    }
    return render(request, 'store/index.html', context=context)

def catalog(request, category_code):
    product = Product.objects.filter(category_id=category_code, is_available=True)
    category = Category.objects.all()

    context = {
        'title': 'Категория ',
        'product': product,
        'category': category,
    }
    return render(request, 'store/product.html', context=context)

def detail(request, code):
    product = get_object_or_404(Product, id=code)
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
        'title': product.name,
    }
    return render(request, 'store/product_detail3.html', context=context)


def order(request, code):
    product = get_object_or_404(Product, id=code)
    category = Category.objects.all()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            product = Product.objects.get(id=code)
            order_form.instance.product = product
            order_form.save()
            return redirect('homepage')
    else:
        order_form = OrderForm()
    context = {
        'title': 'Заказ',
        'category': category,
        'order_form': order_form,
        'product': product,
    }
    return render(request, 'store/order.html', context=context)