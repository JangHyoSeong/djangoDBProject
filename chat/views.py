from django.shortcuts import render, redirect
from .models import ChatRoom
from .models import ProductPost

def chatroom(request):
    return render(request, 'chat/chatroom.html')

