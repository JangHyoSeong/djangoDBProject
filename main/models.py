from django.db import models


class User(models.Model):
    UID = models.CharField(max_length = 20, primary_key=True)
    nickname = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=15, default = '')
    email = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nickname



class ProductPost(models.Model):
    product_ID = models.CharField(max_length = 20, primary_key=True)
    price = models.PositiveIntegerField(default = 0)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=10, null=True)
    postTitle = models.CharField(max_length=30, default='')
    postTime = models.DateTimeField(auto_now_add=True)
    postContents = models.TextField()
    productImage = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.postTitle

    
class ChatRoom(models.Model):
    chatRoomID = models.CharField(max_length=20, primary_key=True)

class Chat(models.Model):
    chatID = models.CharField(max_length=20, primary_key=True)
    contents = models.TextField()
    chatTime = models.DateTimeField()
    reading = models.BooleanField()
    chatType = models.BooleanField()

    
    

