from django .urls import path
from . import views




app_name="videos"

urlpatterns = [
    path("detail/<int:pk>/", views.VideoDetail.as_view(), name="detail" ),
    path("update/<int:pk>/", views.VideoUpdate.as_view(), name="update" ),
    path("delete/<int:pk>/", views.VideoDelete.as_view(), name="delete" ),
    path("mylist/", views.MylistVideo.as_view(), name="mylist" ),
    path("upload/", views.VideoUpload.as_view(), name="upload" ),
    
    
    
]