from django.urls import path
from .views import *
urlpatterns = [
    path('create', CreateProduct, name="create"),
    path('', GetProduct, name="get")
]