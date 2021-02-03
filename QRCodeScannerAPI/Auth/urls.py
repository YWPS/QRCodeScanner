from django.urls import path
from .views import *
urlpatterns = [
    path('create/<username>', CreateUser, name='create'),
    path('get/<username>', GetUser, name='get'),
    path('updateusername', UpdateUsername, name="update"),
    path('updatepassword', UpdatePassword, name="update"),
    path('delete/<username>', DeleteUser, name="delete"),
    path('auth/<username>', AuthUser, name="auth")
]