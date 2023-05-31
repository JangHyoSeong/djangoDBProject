from django.db import models
from users.models import User
from main.models import *

class ChatRoom(models.Model):
    chatRoomID = models.AutoField(primary_key=True)



class Chat(models.Model):
    chatID = models.AutoField(primary_key=True)
    contents = models.TextField()
    chatTime = models.DateTimeField(auto_now_add=True)
    reading = models.BooleanField()

class Send(models.Model):
    chatRoomID = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    chatID = models.ForeignKey(Chat, on_delete=models.CASCADE)