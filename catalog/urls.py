from django.urls import path

from catalog.views import contacts, home
from . import views


urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('<int:product_id>', views.product_detail, name='detail'),
    path('', views.product_list, name='list'),
]