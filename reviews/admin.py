from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display=("user", "video",)
    
    
    
