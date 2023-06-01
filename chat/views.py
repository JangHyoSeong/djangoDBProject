from django.shortcuts import render, redirect
from .models import ChatRoom
from .models import ProductPost

def chatroom(request, pk):
    posting = ProductPost.objects.get(pk=pk)
    new_chatroom = None

    if request.method == 'POST':
        new_chatroom = ChatRoom.objects.create(
            userID=request.user,
            postID=posting,
        )
        return redirect('chat:chatroom', pk=new_chatroom.pk)  # pk 값을 전달하여 redirect

    context = {'posting': posting, 'chatroom': new_chatroom}
    return render(request, 'chat/chatroom.html', context)
