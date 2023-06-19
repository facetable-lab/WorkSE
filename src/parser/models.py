import json

from django.db import models


def default_urls():
    return {
        'head_hunter': '',
        'habr_career': ''
    }


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
    """Модель языков программирования"""
    name = models.CharField('Язык программирования', max_length=50)
    slug = models.CharField(max_length=60, blank=True, verbose_name='URL', unique=True)

    def __str__(self):
        """Строковое представление объекта, в т.ч и в админке"""
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


class Vacancy(models.Model):
    """Модель населенных вакансий"""
    url = models.URLField()
    title = models.CharField('Должность', max_length=250)
    company = models.CharField('Компания', max_length=250)
    description = models.TextField(verbose_name='Описание')
    timestamp = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')

    def __str__(self):
        """Строковое представление объекта, в т.ч и в админке"""
        return self.title

    class Meta:
        """Отображение названия модели в админке"""

        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Error(models.Model):
    """Модель ошибок"""
    timestamp = models.DateField(auto_now_add=True, verbose_name='Время')
    data = models.JSONField(default={}, verbose_name='Данные')

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class PrettyJSONEncoder(json.JSONEncoder):
    """Выравнивание внещнего вида данных в поле Json модели Url"""

    def __init__(self, *args, indent, sort_keys, **kwargs):
        super().__init__(*args, indent=4, sort_keys=True, **kwargs)


class Url(models.Model):
    """Модель ссылок на сайты-первоисточники"""
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык программирования')
    url_data = models.JSONField(default=default_urls, verbose_name='Маршруты', encoder=PrettyJSONEncoder)

    def __str__(self):
        return f'{self.city} | {self.language}'

    class Meta:
        unique_together = ('city', 'language')

        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
