from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "home.html", context=context)


def contacts(request):
    return render(request, "contacts.html")


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "product_page.html", context=context)
