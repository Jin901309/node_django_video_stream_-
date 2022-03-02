from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from . import models
from subscribes.models import SubscribesModel
from etcs.models import Likes
# Create your views here.
class MyChannel(DetailView):
    model = models.Channel
    template_name="channels/channel_detail.html"
    context_object_name="channel"
    
    

    
    
    
    
class UpdateChannel(UpdateView):
    model=models.Channel
    template_name="channels/channel_update.html"
    fields=(
        "name",
        "main_image",
        
    )
    success_message="채널 변경 완료"
    def  get_object( self, queryset = None ): 
        #자기자신을 리턴
        return self.request.user.channels
    
    


    
    