# Generated by Django 3.2.3 on 2021-10-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0008_sight_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
