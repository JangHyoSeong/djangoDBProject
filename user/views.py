from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from user.models import User

def mypage(request):
    return render(request, 'user/mypage.html')