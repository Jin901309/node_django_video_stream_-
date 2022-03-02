from django import forms
from . import models

class VideoUpdateForm(forms.ModelForm):
    
    class Meta:
        model = models.VideoModel
        fields = ("title", "description", "file", "thumbnailimage",)
        help_texts = {
            'file': '*.mp4파일만 가능',
        }



class CreateVideo(forms.ModelForm):
    
    
    
    class Meta:
        model=models.VideoModel
        fields = ("title", "description", "file", "thumbnailimage",)
        help_texts = {
            'file': '*.mp4파일만 가능',
        }
        
        
        
    def save(self, *args, **kwargs):
        video=super().save(commit=False)
        return video