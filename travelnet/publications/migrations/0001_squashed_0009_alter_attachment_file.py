# Generated by Django 3.2.13 on 2022-05-28 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    replaces = [('publications', '0001_initial'), ('publications', '0002_alter_publication_post_referred_to'), ('publications', '0003_auto_20220517_0120'), ('publications', '0004_auto_20220520_0155'), ('publications', '0005_auto_20220523_0431'), ('publications', '0006_auto_20220525_0029'), ('publications', '0007_alter_publication_location'), ('publications', '0008_alter_attachment_file'), ('publications', '0009_alter_attachment_file')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('visible', models.BooleanField(default=True, verbose_name='Видимость')),
                ('text', models.TextField(verbose_name='Текст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': [37.60024739728942, 55.763870740960954], 'language': 'ru', 'placeholder': 'Выберите геопозицию на карте', 'zoom': 7}, verbose_name='Расположение')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('file', models.ImageField(upload_to='attachments/', verbose_name='Приложение')),
                ('file_type', models.CharField(choices=[('Photo', 'Фото'), ('Video', 'Видео')], default='Photo', max_length=10, verbose_name='Тип файла')),
                ('publication', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publications.publication', verbose_name='Публикация')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Вложение',
                'verbose_name_plural': 'Вложения',
            },
        ),
    ]
