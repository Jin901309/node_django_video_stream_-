from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ..models import VideoModel 


class VideoSerializer(ModelSerializer):
    class Meta:
        model=VideoModel
        fields=('id','title', 'description','file','thumbnailimage')