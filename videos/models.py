from django.db import models
from core import models as core_models
from django.utils.translation import gettext_lazy as _
from .validators import validate_file_extension
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone
from . import utills
from hitcount.models import HitCountMixin, HitCount


# Create your models here.
class VideoModel(core_models.TimeStampModel, HitCountMixin):
    title=models.CharField(_("제목"), max_length=64)
    description=models.TextField(_("상세설명"),null=True, blank=True)
    file=models.FileField(upload_to='video/', validators=[validate_file_extension])
    thumbnailimage=models.ImageField(_("썸네일이미지"), upload_to='thumbnail', default="")
    user=models.ForeignKey('users.User', related_name="videomodel", on_delete=models.CASCADE)
    # allow_ip=models.GenericIPAddressField(default="", null=True)

    class Meta:
        db_table='videos'
        verbose_name='영상'
        verbose_name_plural='영상'
        
        
    def __str__(self) -> str:
        return f'영상제목:{str(self.title)}-{str(self.user.email)}'
    
    def get_absolute_url(self):
        return reverse("videos:detail", kwargs={"pk":self.pk})
    
    
    
    #데이터 삭제시 파일도 자동 삭제
    def delete(self, *args, **kargs):
        # import os
        # from django.conf import settings
        # if self.file:
        #     os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))
        self.file.close()
        self.file.delete()
        self.thumbnailimage.delete()
        
        super(VideoModel, self).delete(*args, **kargs)
        
        
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
        