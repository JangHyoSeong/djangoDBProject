from django.contrib import admin
from .models import User, ProductPost, ChatRoom, Chat


admin.site.register(User)
admin.site.register(ProductPost)
admin.site.register(ChatRoom)
admin.site.register(Chat)