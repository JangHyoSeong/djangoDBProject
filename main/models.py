from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductPost(models.Model):
    product_ID = models.AutoField(primary_key=True)
    price = models.PositiveIntegerField(default = 0)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=10, null=True)
    postTitle = models.CharField(max_length=30, default='')
    postContents = models.TextField()
    productImage = models.ImageField(blank=True, null=True)

    STATUS_CHOICE=(
        (0,'판매중'),
        (1,'판매 진행중'),
        (2,'판매 완료'),
    )
    STATUS_SECTION = [MaxValueValidator(2),MinValueValidator(0)]
    status = models.IntegerField(validators=STATUS_SECTION, choices = STATUS_CHOICE, default=0)

    def __str__(self):
        return self.postTitle
    
class Upload(models.Model):
    uploadID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="userID")
    postID = models.ForeignKey(ProductPost,related_name="post", on_delete=models.CASCADE, db_column="postID")
    postingTime = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(ProductPost, on_delete=models.CASCADE)

class SalesHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(ProductPost, on_delete=models.CASCADE)

class PurchaseHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(ProductPost, on_delete=models.CASCADE)

    
    

