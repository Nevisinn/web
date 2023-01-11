from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analytics'
    verbose_name = 'Аналитика профессий'

class GeographyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'geography'
    verbose_name = 'География'