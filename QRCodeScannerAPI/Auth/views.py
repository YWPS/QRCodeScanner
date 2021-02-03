from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import json
# Create your views here.
def CreateUser(request, username):
    if request.method == "POST":
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        password = jsonData["password"]
        User.objects.create_user(username=username, password=password)
        return JsonResponse({})

def GetUser(request, username):
    target = User.objects.get(username)
    return JsonResponse(
        {
            "username": target.username
        }
    )
def UpdateUsername(request):
    if request.method == "POST":
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        oldusername = jsonData["oldusername"]
        newusername = jsonData["newusername"]
        target = User.objects.get(username=oldusername)
        target.username = newusername
        target.save()
        return JsonResponse({})
def UpdatePassword(request):
    if request.method == "POST":
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        username = jsonData["username"]
        newpassword = jsonData["newpassword"]
        target = User.objects.get(username=username)
        target.set_password(newpassword)
def DeleteUser(request, username):
    if request.method == "POST":
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        username = jsonData["username"]
        User.objects.delete(username=username)
        return JsonResponse({})
def AuthUser(request, username):
    if request.method == "POST":
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        username = jsonData["username"]
        password = jsonData["password"]
        if authenticate(username=username, password=password)is None:
            return JsonResponse({
                "fail": True
            })
        return JsonResponse({
                "fail": True
            })