from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .models import Products, Order
from .forms import OrderForm


def home(request):
    products = Products.objects.all()
    return render(request, "home.html", {"products":products})

def product(request, product_id=0):
    try:
        product = Products.objects.get(id=product_id)
    except:
        return HttpResponseNotFound("<h1>404 - Product not found</h1>")
    return render(request, "product.html", {"product": product})

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")

def order_form(request):

    product_id = request.GET.get('product_id')

    if request.method == 'POST':
        order = OrderForm(request.POST)

        if order.is_valid():
            if product_id in request.POST:
                product_id = request.POST.get('product_id')
            order.instance.product_id = product_id
            order.save()
            return redirect('thank_you')

    else:
        order = OrderForm()

    return render(request, 'order_form.html', {"order": order, 'product_id': product_id})

def thank_you(request):
    return render(request, 'thank_you.html')