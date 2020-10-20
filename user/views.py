from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    print("这是第一个视图")

    return HttpResponse("KO")


def user_login(request):
    print("这是dev上的视图")

    return HttpResponse("yes")


def test(request):
    print("这是测试视图")

    return HttpResponse("测试")
