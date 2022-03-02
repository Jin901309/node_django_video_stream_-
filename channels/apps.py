from django.apps import AppConfig


class ChannelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'channels'
    verbose_name='채널명(유저생성시 자동생성)'
