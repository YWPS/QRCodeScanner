import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.hashers import check_password

from .models import Product

"""
GET DATA
"""
@csrf_exempt
def CreateProduct(request):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        name = jsonData["name"]
        code = str(jsonData["code"])
        username = jsonData["username"]
        # get user
        user = User.objects.get(username=username)
        hash = get_random_string(length=40)
        # update or create model
        Product.objects.update_or_create(name=name, code=code, user=user,  hash=hash)
        # response
        return JsonResponse({
            "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=256x256"
        })



@csrf_exempt
def GetProduct(request):
    if request.method == "POST":
            # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # json data
        hash = jsonData["hash"]
        target = Product.objects.get(hash=hash)
        data = {
            'Name': target.name,
            'Code': eval(target.code),
            'Person': target.person.username
        }
        return JsonResponse(data)




"""
USER AUTHENTICATION
"""