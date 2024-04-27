from django.urls import path
from .views import main, product_add

urlpatterns = [
    path('', main, name='main'),
    path('add/', product_add, name='add')
]
