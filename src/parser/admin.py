from django.contrib import admin

from . import models


class CityAdmin(admin.ModelAdmin):
    """Отображение и функционал модели City в админке"""

    # Генерация слага
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.City, CityAdmin)
