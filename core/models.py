from django.db import models
from django.utils.translation import gettext_lazy as _
from . import managers

# Create your models here.
class TimeStampModel(models.Model):
    created=models.DateTimeField(verbose_name='등록시간',auto_now_add=True)
    updated=models.DateTimeField(verbose_name='수정시간',auto_now=True)
    objects=managers.CustomModelManager()
    class Meta:
        
        abstract=True
    
    