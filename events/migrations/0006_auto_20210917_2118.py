# Generated by Django 3.2.3 on 2021-09-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_cafe_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainment',
            name='test',
            field=models.BooleanField(default=False, verbose_name='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='test',
            field=models.BooleanField(default=False, verbose_name='test'),
            preserve_default=False,
        ),
    ]
