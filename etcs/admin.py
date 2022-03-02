from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display=('l_video', 'counting',)
    list_per_page=20
    filter_horizontal=(
        "l_user",
        
    )
    raw_id_fields=("l_video",)
    
    
  
