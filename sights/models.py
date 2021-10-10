from django.db import models


class Category(models.Model):
    category_name = models.CharField('Категория', max_length=250)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Sight(models.Model):
    title = models.CharField('Название', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField('URL', max_length=255, unique=True)
    views = models.PositiveIntegerField('Просмотры', default=0)
    full_text = models.TextField('Текст', blank=True)
    price = models.CharField('Стоимость билета', max_length=255, blank=True, help_text='Стоимость билета для музеев')
    adress = models.CharField('Адрес', max_length=255, blank=True)
    schedule = models.CharField('График работы', max_length=255, blank=True)
    number = models.CharField('Номер телефона', max_length=255, blank=True)
    site = models.CharField('Сайт', max_length=255, blank=True)
    image_preview = models.ImageField('Изображение')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


class SightImage(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, verbose_name='Достопримечательность')
    image = models.ImageField('Изображение')

    def __str__(self):
        return f"Название: {self.sight.title} [ID: {self.sight.id}]"

    class Meta:
        verbose_name = 'Достопримечательности фото'
        verbose_name_plural = 'Достопримечательности фото'
