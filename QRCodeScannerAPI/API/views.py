import json

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Product


@csrf_exempt
def CreateProduct(request, name):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        code = str(jsonData["code"])
        username = jsonData["username"]
        # authenticate user
        user = User.objects.get(username=username)
        hash = get_random_string(length=40)
        # update or create model
        Product.objects.update_or_create(name=name, code=code, user=user,  hash=hash)
        # response
        return JsonResponse({
            "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=1024*1024"
        })



@csrf_exempt
def GetProduct(request, hash):
    if request.method == "POST":
        target = Product.objects.get(hash=hash)
        data = {
            'name': target.name,
            'code': eval(target.code),
            'user': target.person.username
        }
        return JsonResponse(data)



@csrf_exempt
def UpdateProduct(request, hash):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        name = jsonData["name"]
        code = str(jsonData["code"])
        username = jsonData["username"]
        # authenticate user
        user = User.objects.get(username=username)
        # update or create model
        Product.objects.update_or_create(name=name, code=code, user=user,  hash=hash)
        # response
        return JsonResponse({
            "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=1024*1024"
        })

@csrf_exempt
def DeleteProduct(request, hash):
    Product.objects.delete(hash=hash)
    return JsonResponse({})
