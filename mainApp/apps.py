from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainApp'




#referal link apps.py
from django.apps import AppConfig

class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainApp'

    def ready(self):
        import mainApp.signals  # Ensure the signal is loaded
