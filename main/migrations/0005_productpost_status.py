# Generated by Django 4.2.1 on 2023-05-30 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_chat_delete_chatroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpost',
            name='status',
            field=models.IntegerField(choices=[(0, '판매중'), (1, '판매 진행중'), (2, '판매 완료')], default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)]),
        ),
    ]