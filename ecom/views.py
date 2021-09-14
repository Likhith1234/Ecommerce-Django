from django import contrib
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    context = {}
    return render(request, "main.html", context)

def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    return render(request, "cart.html", context={"items": items, "order": order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    return render(request, "checkout.html", context={"items": items, "order": order})