from django.urls import path
from .views import *
urlpatterns = [
    path('create/<name>', CreateUser, name='create'),
    path('get/<hash>', GetUser, name='get'),
    path('update/<hash>', UpdateUserUsername, name="update"),
    path('update/<hash>', UpdateUserPassword, name="update"),
    path('delete/<hash>', DeleteUser, name="delete")
]