from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # Отображение названия приложения в админке
    verbose_name = 'Аккаунты'
