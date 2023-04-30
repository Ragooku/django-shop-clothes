from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('catalog/<int:category_code>', catalog, name='catalog'),
    path('product/<int:code>', detail, name='detail'),
    path('order/<int:code>', order, name='order'),
]