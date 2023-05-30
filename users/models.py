from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=200, null=True)
    profileImage = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username
'''
    다음 User 속성들은 django auth.models에서 기본 제공
    username
    password
    email
    Date joined
'''

