from django.shortcuts import render
import datetime
import json
import os

def get_data():
    try:
        data = json.load(open(os.path.abspath('geekshop\data.json'), encoding="utf-8"))
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
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": get_data()}
    return render(request, "mainapp/contact.html", content)
