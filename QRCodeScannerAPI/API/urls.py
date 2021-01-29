from django.urls import path
from .views import *
urlpatterns = [
    path('create/<name>', CreateProduct, name='create'),
    path('get/<hash>', GetProduct, name='get'),
    path('update/<hash>', UpdateProduct, name="update"),
    path('delete/<hash>', DeleteProduct, name="delete")
]