# Generated by Django 3.2.13 on 2022-05-23 01:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0004_auto_20220520_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='publication',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='publications.publication', verbose_name='Публикация'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='Автор'),
        ),
    ]
