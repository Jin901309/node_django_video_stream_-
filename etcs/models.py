from django.db import models
from core import models as core_models
from django.dispatch import receiver
from django.db.models.signals import post_save
from videos.models import VideoModel
# Create your models here.
class Likes(core_models.TimeStampModel):
    l_video=models.OneToOneField('videos.VideoModel',related_name='like', on_delete=models.CASCADE,verbose_name='영상')
    l_user=models.ManyToManyField('users.User', related_name='like', blank=True)
    
    def __str__(self):
        return f'{self.l_video}'
    
    class Meta:
        verbose_name='좋아요'
        verbose_name_plural='좋아요'
        
        
    def counting(self):
        return self.l_user.count()
    
    counting.short_description="좋아요"
    
@receiver( post_save, sender = VideoModel )
def video_post_save( sender, instance, created, *args, **kwargs ):
    if created:
        like, _=Likes.objects.get_or_create(l_video=instance)
        like.save()
        
        
    
        


    
    

    
