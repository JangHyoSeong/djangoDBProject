from django.shortcuts import render, redirect
from .models import ChatRoom, createChatRoom
from .models import ProductPost

def chatroom(request):
    return render(request, 'chat/chatroom.html')

def create_chatroom(request, pk):
    if request.method == 'POST':
        new_chatroom = ChatRoom.objects.create()
        post = ProductPost.objects.get(pk=pk)

        new_createchatroom = createChatRoom.objects.create(
            chatRoomID=new_chatroom,
            productID=post,
            userID=request.user,
        )

        return redirect('posting')
    return render(request, 'chat/chatroom.html')
