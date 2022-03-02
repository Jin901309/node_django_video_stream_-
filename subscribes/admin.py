from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.SubscribesModel)
class SubsVideoAdmin(admin.ModelAdmin):
    list_display=('users', 'counting_channel',)
    list_per_page=20
    
    
    # fieldsets =(
    #     (
    #         "소유주",
    #         {"fields": ("users", )},
            
    #     ),
    #     ("자세한 정보",
    #         {
    #             #감추기 기능 접기,펼치기
    #             "classes": ("collapse",),
    #             "fields": ("channel",),
    #         },
    #     ),
    # )
    
    filter_horizontal=(
        "channel",
        
    )
    
@admin.register(models.SubscribesCountModel)
class SubscountVideoAdmin(admin.ModelAdmin):
    list_display=('subscribes', 'counting_channel',)
    list_per_page=20
    
    filter_horizontal=(
        "user",
    )
    
