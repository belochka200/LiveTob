# Generated by Django 3.2.3 on 2021-09-13 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('recomended', models.BooleanField(default=False, verbose_name='Рекомандовано')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адресс')),
                ('schedule', models.CharField(blank=True, max_length=255, verbose_name='График работы')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')),
                ('site', models.CharField(blank=True, max_length=255, verbose_name='Сайт')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image_preview', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Кафе',
                'verbose_name_plural': 'Кафе',
            },
        ),
        migrations.CreateModel(
            name='CafeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория кафе',
                'verbose_name_plural': 'Категории кафе',
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('recomended', models.BooleanField(default=False, verbose_name='Рекомандовано')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адресс')),
                ('schedule', models.CharField(blank=True, max_length=255, verbose_name='График работы')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')),
                ('site', models.CharField(blank=True, max_length=255, verbose_name='Сайт')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image_preview', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Развлечение',
                'verbose_name_plural': 'Развлечения',
            },
        ),
        migrations.CreateModel(
            name='EntertainmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория развлечения',
                'verbose_name_plural': 'Категории развлечений',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('recomended', models.BooleanField(default=False, verbose_name='Рекомандовано')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адресс')),
                ('schedule', models.CharField(blank=True, max_length=255, verbose_name='График работы')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')),
                ('site', models.CharField(blank=True, max_length=255, verbose_name='Сайт')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image_preview', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.CreateModel(
            name='HotelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория отеля',
                'verbose_name_plural': 'Категории отелей',
            },
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Отель изображение',
                'verbose_name_plural': 'Отель изображения',
            },
        ),
        migrations.AddField(
            model_name='hotel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.hotelcategory', verbose_name='Категория отеля'),
        ),
        migrations.CreateModel(
            name='EntertainmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('ent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.entertainment', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Место изображение',
                'verbose_name_plural': 'Место изображения',
            },
        ),
        migrations.AddField(
            model_name='entertainment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.entertainmentcategory', verbose_name='Категория отеля'),
        ),
        migrations.CreateModel(
            name='CafeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.cafe', verbose_name='Кафе')),
            ],
            options={
                'verbose_name': 'Кафе изображение',
                'verbose_name_plural': 'Кафе изображения',
            },
        ),
        migrations.AddField(
            model_name='cafe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.cafecategory', verbose_name='Категория кафе'),
        ),
    ]
