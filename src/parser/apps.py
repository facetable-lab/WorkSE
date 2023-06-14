from django.apps import AppConfig


class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parser'

    # Отображение названия приложения в админке
    verbose_name = 'Поисковая система'
