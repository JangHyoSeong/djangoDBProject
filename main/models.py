from django.db import models


class ProductPost(models.Model):
    product_ID = models.AutoField(primary_key=True)
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
    chatRoomID = models.AutoField(primary_key=True)

class Chat(models.Model):
    chatID = models.AutoField(primary_key=True)
    contents = models.TextField()
    chatTime = models.DateTimeField()
    reading = models.BooleanField()
    chatType = models.BooleanField()

    
    

