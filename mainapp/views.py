from django.shortcuts import render
import datetime
import json
import os

def get_data():
    try:
        data = json.load(open(os.path.abspath(r'geekshop\data.json'), encoding="utf-8"))
    except:
        data = []
    return data

def main(request):
    title = "главная"
    content = {"title": title, "products": get_data()}
    return render(request, 'mainapp/index.html', content)

def products(request):
    title = "продукты"
    content = {"title": title, "data": get_data()}
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    content = {"title": title, "visit_date": visit_date, "locations": get_data()}
    return render(request, "mainapp/contact.html", content)
