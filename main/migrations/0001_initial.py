# Generated by Django 4.2.1 on 2023-05-31 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPost',
            fields=[
                ('product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('postTitle', models.CharField(default='', max_length=30)),
                ('address', models.CharField(max_length=100, null=True)),
                ('postContents', models.TextField(max_length=100)),
                ('category', models.CharField(max_length=10, null=True)),
                ('productImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.PositiveIntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, '판매중'), (1, '판매 진행중'), (2, '판매 완료')], default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SalesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TradingReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewRating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('uploadID', models.AutoField(primary_key=True, serialize=False)),
                ('postingTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productpost')),
            ],
        ),
    ]
