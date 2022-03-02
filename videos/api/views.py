from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import VideoModel 
from .serializers import VideoSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/videos',
        'GET /api/videos/:id',
    ]
    
    return Response(routes)

@api_view(['GET'])
def getVideos(request):
    video=VideoModel.objects.all()
    serializer=VideoSerializer(video, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getVideo(request, pk):
    video=VideoModel.objects.get_or_none(id=pk)
    serializer=VideoSerializer(video, many=False)
    return Response(serializer.data)