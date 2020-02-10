from django.shortcuts import render

content = ['aaa', 'bbb']

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
