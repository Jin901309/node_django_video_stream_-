from django.apps import AppConfig


class SubscribesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscribes'
    verbose_name='구독정보(유저생성시 자동생성)'
