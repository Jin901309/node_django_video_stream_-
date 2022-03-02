from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display=("name", "user","created", "updated","channel_is_active",)
    list_filter=("user",)
    filter_horizontal = ('video',)
    
    
    
    
    
    
    