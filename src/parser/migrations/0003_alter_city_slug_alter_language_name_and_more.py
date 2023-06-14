# Generated by Django 4.2.2 on 2023-06-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_language_alter_city_options_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=60, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Язык программирования'),
        ),
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.CharField(blank=True, max_length=60, verbose_name='URL'),
        ),
    ]
