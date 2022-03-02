from django.contrib import admin
from . import models
from django.utils.html import format_html
from django import forms

class VideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text='메인 타이틀 제목을 입력해주세요'
        self.fields['file'].help_text='올릴려는 동영상 파일 (mp4,avi,wmv)파일만가능'
        self.fields['thumbnailimage'].help_text='메인 썸네일 이미지'
        
 
        
    

# Register your models here.
@admin.register(models.VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    form=VideoForm
    list_display=('simplification_title', 'created', 'updated','simplification_description','image_thumbnailimage',)
    #20개씩만 봄
    search_fields = ('title', 'description', )
    raw_id_fields=("user",)
    list_per_page=20
    
    
    @admin.display(description='제목')
    def simplification_title(self, obj):
        return f'{obj.title[:15]}'
    
    
    @admin.display(description='상세설명')
    def simplification_description(self, obj):
        return f'{obj.description[:15]}'
    
    @admin.display(description='썸네일이미지')
    def image_thumbnailimage(self, obj):
        return format_html(
            '<img src="{}" style="width: 40px; height: 40px;" alt="">',
            obj.thumbnailimage.url,
        )
    