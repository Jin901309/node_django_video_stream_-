from django.shortcuts import render
from django.views.generic import  View, DeleteView
from django.http import JsonResponse
from . import models
from videos.models import VideoModel
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
import json


# Create your views here.
class EditView(View):
    def post(self, request, *args, **kwargs): 
        video_id=request.POST.get("videopk", None)
        review=request.POST.get("review", None)
        
        video_obj=get_object_or_404(VideoModel, id=video_id)
        create=models.ReviewModel.objects.create(user=request.user, video=video_obj, post=review)
        a=str(create.id)
        print(create.id)
        

        
        respon=serializers.serialize("json", [create], ensure_ascii=False)
        
        res=json.loads(respon)[0]
        print(res)
        
        return JsonResponse(res, status=200)
    
    
class DeleteView(DeleteView):
    model =models.ReviewModel
    context_object_name = 'review'
    template_name="reviews/review_delete.html"
    
    
    def get_success_url(self):
        return reverse('videos:detail', kwargs={'pk':self.object.video.pk})