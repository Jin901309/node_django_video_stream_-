from django.db import models
from core import models as core_models
from django.db.models.signals import post_save
from django.dispatch import receiver
from videos.models import VideoModel
from users.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# from django.shortcuts  import reverse


# Create your models here.
class Channel(core_models.TimeStampModel):
    name=models.CharField(_("채널명"),max_length=30)
    user=models.OneToOneField('users.User', related_name="channels", on_delete=models.CASCADE, verbose_name="유저", )
    video=models.ManyToManyField('videos.VideoModel', related_name="channels", verbose_name="내 영상목록", blank=True)
    channel_is_active=models.BooleanField(default=True, verbose_name="채널 활성화",)
    main_image=models.ImageField(upload_to="channelimg", verbose_name='채널이미지', blank=True)
    
    class Meta:
        db_table="channels"
        verbose_name="내채널"
        verbose_name_plural="내채널"
    
    def get_absolute_url(self): 
        return reverse('channels:mychan', kwargs={"pk": self.pk})
    
        
        
    def __str__(self) -> str:
        return str(self.name)
    
    
    
    
    
 
 
 #유저 생성시 채널 자동생성
@receiver( post_save, sender = User )
def user_post_save( sender, instance, created, *args, **kwargs ):
    if created:
        obj, create_obj=Channel.objects.get_or_create(user=instance, name=instance.nickname)
        if create_obj:
            obj.name=instance.nickname
            obj.channel_is_active=True
            obj.save()   
    


# 영상 업로드시 채널에 영상정보 자동저장
@receiver( post_save, sender = VideoModel )
def video_post_save( sender, instance, created, *args, **kwargs ):
    user = instance.user.id
    chan=Channel.objects.get_or_none(user=user)
    if chan is not None:
        chan.video.add(instance)
        chan.save()

    
    

    
    
    
