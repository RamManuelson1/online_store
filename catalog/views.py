from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Магазин'
    }

class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = 'Продукты'

class ProductCreateView(CreateView):
    extra_context = {
        'title': 'Создать продукт'
    }
    model = Product
    fields = ('Название', 'описание', 'фото', 'цена', 'категория')
    success_url = reverse_lazy('catalog: catalog_products')