from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View, DetailView, ListView
from django.shortcuts import get_object_or_404
from . import models
from users.models import User
# Create your views here.
class LikeAjax(View):
    def get(self, *args, **kwargs): 
        if self.request.method == "GET":
           like=self.request.GET.get('like', None)
           
           count=get_object_or_404(models.Likes, id=self.kwargs['pk'])
           if str(like)=="true":
                if count:
                    count.l_user.add(self.request.user)
                    count.save()
                    return JsonResponse({'like':'true'}, status=200)
           elif str(like)=="false":
                if count:
                    count.l_user.remove(self.request.user)
                    count.save()
                    return JsonResponse({'like':'false'}, status=200)
                

                

class Likelist(ListView):
    model=models.Likes
    template_name="etcs/likelist.html"
    context_object_name="likes"
    
    def get_queryset(self):
        queryset = models.Likes.objects.all().filter(l_user=self.request.user.pk)
        return queryset
        
                    
                    
                    
        
                    
               
                   
                   
               
            