import json
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.crypto import get_random_string
# Create your views here.
def CreateProduct(request):
    """
    JSON Format:
    {
        'productName': 'Name",
        'productCode': [
            {'name' : 'ABC',
            'code': 1
            },
            {'name' : 'ABC',
            'code': 1
            }
        ]
    }
    """
    if request.method == "POST":
        if request.json:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            id = get_random_string(length=40)
            return JsonResponse({
                "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=256x256"
            })
