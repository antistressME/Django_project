from django.urls import path

from catalog.apps import CatalogConfig

from .views import ContactsTemplateView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("product_page/<int:pk>/", ProductDetailView.as_view(), name="product_page"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
