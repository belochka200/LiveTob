from django.db import models

class PopularPeople(models.Model):
    name = models.CharField("Имя", max_length=255)
    bored = models.CharField("Дата рождения", max_length=255)
    text = models.TextField("Текст")
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Популярный тоболяк'
        verbose_name_plural = 'Популярные тоболяки'

class InterestingFact(models.Model):
    text = models.TextField("Текст")
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Интересный факт'
        verbose_name_plural = 'Интересные факты'
