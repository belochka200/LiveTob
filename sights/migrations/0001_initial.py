# Generated by Django 3.2.3 on 2021-09-04 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('full_text', models.TextField(blank=True, verbose_name='Текст')),
                ('adress', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('schedule', models.CharField(blank=True, max_length=255, verbose_name='График работы')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')),
                ('site', models.CharField(blank=True, max_length=255, verbose_name='Сайт')),
                ('image_preview', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sights.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='SightImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sights.sight', verbose_name='Достопримечательность')),
            ],
            options={
                'verbose_name': 'Достопримечательности фото',
                'verbose_name_plural': 'Достопримечательности фото',
            },
        ),
    ]
