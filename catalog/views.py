from django.views.generic import DetailView, ListView, TemplateView

from config.settings import BASE_DIR

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = BASE_DIR / "catalog/templates/home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = BASE_DIR / "catalog/templates/contacts.html"
    context_object_name = "contacts"


class ProductDetailView(DetailView):
    model = Product
    template_name = BASE_DIR / "catalog/templates/product_page.html"
    context_object_name = "products"
