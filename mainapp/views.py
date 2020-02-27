from django.conf import settings

from django.shortcuts import render
from django.utils import timezone

from .models import Product, ProductCategory, Contacts

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

    products = Product.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()

    content = {
        "title": title, 
        "links_menu":links_menu, 
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, 'mainapp/products.html', content)

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
