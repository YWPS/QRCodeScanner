from django.urls import path
from .views import *
urlpatterns = [
    # GET DATA
    path('create', CreateProduct, name='create'),
    path('get', GetProduct, name='get'),
    # USER AUTHENTICATION
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('login', views.index, name='login')
]