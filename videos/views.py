#-*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views.generic.edit import CreateView
from  . import models, forms
from etcs import models as etcs_models
from reviews import models as review_models
from django.contrib import messages
from hitcount.views import HitCountDetailView






class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        video_list=models.VideoModel.objects.all().order_by("-created")[:10]
        
        context={
            "video_list" : video_list
        }
        """ 클라이언트 시스템의 IP 주소를 가져오기 위해 requestobject를 사용 """ 
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') 
        if x_forwarded_for: 
            ip = x_forwarded_for.split(',')[0] 
        else: 
            ip = request.META.get('REMOTE_ADDR') ### 클라이언트 머신의 실제 IP 주소
            print(ip)
        
        
        
        return render(request, "home.html",context)
    
    
    def post(self, request, *args, **kwargs):
        return render(request, "home.html",{})
    
    
class VideoDetail(HitCountDetailView):
    template_name="videos/video_detail.html"
    context_object_name = 'video'
    count_hit=True
    model=models.VideoModel
    
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['reviews']=review_models.ReviewModel.objects.filter_or_none(video=self.kwargs['pk'])
        context['like_count']=etcs_models.Likes.objects.get_or_none(l_video=self.kwargs['pk'])
        return context
    
    
    
    
class VideoUpdate(UpdateView):
    model=models.VideoModel
    template_name="videos/video_update.html"
    form_class=forms.VideoUpdateForm
    
    
    
    def get_object(self, queryset=None):
        video=super().get_object(queryset=queryset)
        # 방의 주인 id와 유저 id가 다르면 404에러
        if video.user.pk!=self.request.user.pk:
            raise Http404()
        return video
    

class VideoDelete(DeleteView):
    model =models.VideoModel
    context_object_name = 'video'
    template_name="videos/videomodel_confirm_delete.html"
    success_url = reverse_lazy('videos:mylist')
    
    
class MylistVideo(ListView):
    model=models.VideoModel
    context_object_name = 'video_list'
    
    def get_queryset(self):
        queryset = models.VideoModel.objects.filter_or_none(user=self.request.user)
        return queryset
    
    
class VideoUpload(FormView):
    form_class=forms.CreateVideo
    template_name="videos/video_upload.html"
    
    def form_valid(self,form):
        video=form.save()
        video.user=self.request.user
        video.save()
        form.save()
        messages.success(self.request, "영상 업로드 완료")
        return redirect(reverse("videos:mylist"))
    
    
    
    

    
    
    
    
    
    
    
    