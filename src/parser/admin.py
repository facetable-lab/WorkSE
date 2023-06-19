from django.contrib import admin

from . import models


class CityAdmin(admin.ModelAdmin):
    """Отображение и функционал модели City в админке"""

    # Генерация слага
    prepopulated_fields = {'slug': ('name',)}


class LanguageAdmin(admin.ModelAdmin):
    """Отображение и функционал модели Language в админке"""

    # Генерация слага
    prepopulated_fields = {'slug': ('name',)}


# Регистрация модели City
admin.site.register(models.City, CityAdmin)
# Регистрация модели Language
admin.site.register(models.Language, LanguageAdmin)
# Регистрация модели Vacancy
admin.site.register(models.Vacancy)
# Регистрация модели Error
admin.site.register(models.Error)
# Регистрация модели Url
admin.site.register(models.Url)
