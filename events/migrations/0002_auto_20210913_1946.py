# Generated by Django 3.2.3 on 2021-09-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='recomended',
        ),
        migrations.RemoveField(
            model_name='entertainment',
            name='recomended',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='recomended',
        ),
    ]
