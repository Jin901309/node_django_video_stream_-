from django.shortcuts import redirect, render
from videos.models import VideoModel
from channels.models import Channel
from django.db.models import Q

# Create your views here.
def resolve_search(request):
    search=request.POST.get("video_search", None)
    print(search)
    if search:
        video_filter=VideoModel.objects.filter_or_none(title__icontains=search)
        
        if search is not None and str(search) != "":
            if video_filter is not None:
                return render(request, "search.html", {"video_filter": video_filter})
            
    else:
        return redirect("core:home")
        
        
        