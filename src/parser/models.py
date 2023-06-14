from django.db import models


class City(models.Model):
    """Модель населенных пунктов"""
    name = models.CharField('Город', max_length=50)
    slug = models.CharField(max_length=60, blank=True, verbose_name='URL', unique=True)

    def __str__(self):
        """Строковое представление объекта, в т.ч и в админке"""
        return self.name

    class Meta:
        """Отображение названия модели в админке"""

        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Language(models.Model):
    """Модель языков программирования (специальность)"""
    name = models.CharField('Язык программирования', max_length=50)
    slug = models.CharField(max_length=60, blank=True, verbose_name='URL', unique=True)

    def __str__(self):
        """Строковое представление объекта, в т.ч и в админке"""
        return self.name

    class Meta:
        """Отображение названия модели в админке"""

        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
