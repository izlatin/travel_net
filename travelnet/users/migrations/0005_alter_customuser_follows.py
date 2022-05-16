# Generated by Django 3.2.13 on 2022-05-15 12:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='follows',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]