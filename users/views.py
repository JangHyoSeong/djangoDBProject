from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from users.models import User
from users.forms import UserForm
from django.contrib.auth import authenticate, login

def mypage(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'users/mypage.html', {'user' : user})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data['phone']
            nickname = form.cleaned_data['nickname']
            address = form.cleaned_data['address']
            profileImage = form.cleaned_data['profileImage'],
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})