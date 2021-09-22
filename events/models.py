from main import views
from django.db import models


class CafeCategory(models.Model):
    category_name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta():
        verbose_name = 'Категория кафе'
        verbose_name_plural = 'Категории кафе'


class HotelCategory(models.Model):
    category_name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta():
        verbose_name = 'Категория отеля'
        verbose_name_plural = 'Категории отелей'


class EntertainmentCategory(models.Model):
    category_name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta():
        verbose_name = 'Категория развлечения'
        verbose_name_plural = 'Категории развлечений'


class Cafe(models.Model):
    title = models.CharField('Название', max_length=255, blank=True)
    category = models.ForeignKey(CafeCategory, on_delete=models.PROTECT, verbose_name='Категория кафе')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    recomended = models.BooleanField('Рекомандовано')
    views = models.PositiveIntegerField('Просмотры', default=0)
    address = models.CharField('Адресс', max_length=255, blank=True)
    schedule = models.CharField('График работы', max_length=255, blank=True)
    number = models.CharField('Номер телефона', max_length=255, blank=True)
    site = models.CharField('Сайт', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)
    image_preview = models.ImageField('Изображение')
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Кафе'
        verbose_name_plural = 'Кафе'


class Hotel(models.Model):
    title = models.CharField('Название', max_length=255, blank=True)
    category = models.ForeignKey(HotelCategory, on_delete=models.PROTECT, verbose_name='Категория отеля')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    recomended = models.BooleanField('Рекомандовано')
    views = models.PositiveIntegerField('Просмотры', default=0)
    address = models.CharField('Адресс', max_length=255, blank=True)
    schedule = models.CharField('График работы', max_length=255, blank=True)
    number = models.CharField('Номер телефона', max_length=255, blank=True)
    site = models.CharField('Сайт', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)
    image_preview = models.ImageField('Изображение')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Entertainment(models.Model):
    title = models.CharField('Название', max_length=255, blank=True)
    category = models.ForeignKey(EntertainmentCategory, on_delete=models.PROTECT, verbose_name='Категория развлечения')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    recomended = models.BooleanField('Рекомандовано')
    views = models.PositiveIntegerField('Просмотры', default=0)
    address = models.CharField('Адресс', max_length=255, blank=True)
    schedule = models.CharField('График работы', max_length=255, blank=True)
    number = models.CharField('Номер телефона', max_length=255, blank=True)
    site = models.CharField('Сайт', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)
    image_preview = models.ImageField('Изображение')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Развлечение'
        verbose_name_plural = 'Развлечения'


class CafeImage(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='Кафе')
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.cafe.title

    class Meta:
        verbose_name = 'Кафе изображение'
        verbose_name_plural = 'Кафе изображения'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.hotel.title

    class Meta:
        verbose_name = 'Отель изображение'
        verbose_name_plural = 'Отели изображения'


class EntertainmentImage(models.Model):
    ent = models.ForeignKey(Entertainment, on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.ent.title

    class Meta:
        verbose_name = 'Развлечение изображение'
        verbose_name_plural = 'Развлечения изображения'
