# Generated by Django 4.2.2 on 2023-06-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_alter_city_slug_alter_language_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=60, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.CharField(blank=True, max_length=60, unique=True, verbose_name='URL'),
        ),
    ]
