# Generated by Django 3.2.3 on 2021-10-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0007_alter_sight_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='sight',
            name='price',
            field=models.CharField(blank=True, help_text='Стоимость билета для музеев', max_length=255, verbose_name='Стоимость билета'),
        ),
    ]