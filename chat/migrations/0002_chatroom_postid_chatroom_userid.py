# Generated by Django 4.2.1 on 2023-05-31 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='postID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.productpost'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='userID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
