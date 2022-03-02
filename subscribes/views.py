from django.shortcuts import render
from django.views.generic import View, ListView
from . import models
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
class Subplus(View):
     def get(self, *args, **kwargs): 
        if self.request.method == "GET":
           sub=self.request.GET.get('sub', None)
           
           
          #  '구독한 채널'
           count=get_object_or_404(models.SubscribesModel, users=self.request.user)
           
          #  채널구독
           you_channel=get_object_or_404(models.SubscribesCountModel, subscribes=self.kwargs['pk'])
           
           if str(sub)=="true":
                if count:
                    count.channel.add(you_channel.subscribes)
                    you_channel.user.add(self.request.user)
                    count.save()
                    you_channel.save()
                    return JsonResponse({'sub':'true'}, status=200)
           elif str(sub)=="false":
                if count:
                    count.channel.remove(you_channel.subscribes)
                    you_channel.user.remove(self.request.user)
                    count.save()
                    you_channel.save()
                    return JsonResponse({'sub':'false'}, status=200)
               
               
class SubList(ListView):
     model=models.SubscribesModel
     template_name="subscribes/sublist.html"
     context_object_name = "sublist"
     
     

     def get_queryset(self):
        queryset = models.SubscribesModel.objects.get_or_none(users=self.request.user)
        return queryset