from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일")
    phone=forms.CharField(max_length=11)
    nickname=forms.CharField(max_length=10)
    address=forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "phone", "nickname", "address")