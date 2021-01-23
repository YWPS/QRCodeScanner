import json
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.crypto import get_random_string

from .models import Product
# Create your views here.
def CreateProduct(request):
    """
    JSON Format:
    {
    "name": "Coca Cola",
    "code": [
        {
            "name": "Cap",
            "code": 1
        },
        {
            "name": "Bottle",
            "code": 2
        }
    ]
}
    """
    if request.method == "POST":
        if request.json:
            jsonUnicode = request.body.decode('utf-8')
            jsonData = json.loads(jsonUnicode)
            # required fields
            name = jsonData["name"]
            code = str(jsonData["code"])
            id = get_random_string(length=40)
            # update or create model
            Product.objects.update_or_create(name=name, code=code, id=id)
            # response
            return JsonResponse({
                "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=256x256"
            })

def GetProduct(request):
    """
    JSON Format:
    {
        'id': '1234mds'
    }
    """
    if request.method == "POST":
        if request.json:
            jsonUnicode = request.body.decode('utf-8')
            jsonData = json.loads(jsonUnicode)
            id = jsonData["id"]
            target = Product.objects.get(id=id)
            data = {
                'Name': target.name,
                'Code': eval(target.code)
            }
            return JsonResponse(data)
