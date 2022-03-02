from django.db import models
from core import models as core_models
from videos.models import VideoModel
from datetime import datetime, timedelta
from django.utils import timezone
# Create your models here.
class ReviewModel(core_models.TimeStampModel):
    user=models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="review", verbose_name='유저')
    video=models.ForeignKey('videos.VideoModel',on_delete=models.CASCADE, related_name="review", verbose_name='영상')
    post=models.TextField(verbose_name='내용', max_length=256)
    
    class Meta:
        
        verbose_name='메인리뷰'
        verbose_name_plural='메인리뷰'
        
    
    def __str__(self) -> str:
        return str(self.user.nickname)
    
    @property
    def created_string(self):
        time = datetime.now() - self.created

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created.date()
            return str(time.days) + '일 전'
        else:
            return False
    



