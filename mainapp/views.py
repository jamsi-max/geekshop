from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
import random

from .models import Product, ProductCategory, Contacts
from basketapp.models import Basket

# function upload data from file json
# import json
# import os
# def get_data():
#     try:
#         data = json.load(open(os.path.abspath(r'geekshop\data.json'), encoding="utf-8"))
#     except:
#         data = []
#     return data

def main(request):
    title = "главная"

    products = Product.objects.all()[:4]

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]
    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products

def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()

    basket = get_basket(request.user)
    # count = sum([n.quantity for n in Basket.objects.filter(user=request.user)])
    # price = sum([n.product.price for n in Basket.objects.filter(user=request.user)])
    

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")
        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
            # "count": count,
            # "price": price,
        }
        return render(request, "mainapp/products_list.html", content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        "title": title, 
        "links_menu":links_menu, 
        "same_products": same_products,
        "hot_product": hot_product,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        # "count": count,
        # "price": price,
    }
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk),
        "basket": get_basket(request.user),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)

def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contacts.objects.all()
    content = {
        "title": title, 
        "visit_date": visit_date, 
        "locations": locations,
        "media_url": settings.MEDIA_URL,
        }
    return render(request, "mainapp/contact.html", content)
