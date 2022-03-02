from django.db import models
from users.models import User
from core import models as core_models
from channels import models as chan_models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class SubscribesModel(core_models.TimeStampModel):
    users=models.OneToOneField('users.User', related_name='subscribes', on_delete=models.CASCADE, verbose_name='소유주')
    channel=models.ManyToManyField('channels.Channel', related_name='subscribes', verbose_name='구독 채널', blank=True)
    
    class Meta:
        verbose_name='구독한 채널'
        verbose_name_plural='구독한 채널'
        
    def __str__(self):
        return str(self.users)
    
    
    def counting_channel(self):
        return int(self.channel.count())
    
    counting_channel.short_description="구독한 채널수"
    
@receiver( post_save, sender = User )
def user_post_save( sender, instance, created, *args, **kwargs ):
    if created:
        sub, _=SubscribesModel.objects.get_or_create(users=instance)
        sub.save()


   
class SubscribesCountModel(core_models.TimeStampModel):
    subscribes=models.OneToOneField('channels.Channel', related_name='subscribescount', on_delete=models.CASCADE, verbose_name='구독')
    user=models.ManyToManyField('users.User', related_name='subscribescount', verbose_name='구독자 수', blank=True)
    
    class Meta:
        verbose_name='구독자 수'
        verbose_name_plural='구독자 수'
        
    def __str__(self):
        return str(self.subscribes)
    
    def counting_channel(self):
        return self.user.count()
    
    counting_channel.short_description="구독자 수"
    
@receiver( post_save, sender = chan_models.Channel )
def subscribes_post_save( sender, instance, created, *args, **kwargs ):
    if created:
        sub, _=SubscribesCountModel.objects.get_or_create(subscribes=instance)
        sub.save()