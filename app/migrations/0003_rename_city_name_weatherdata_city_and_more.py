# Generated by Django 5.0.2 on 2024-03-13 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_weatherdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='city_name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='weatherdata',
            old_name='temparature',
            new_name='temperature',
        ),
    ]
