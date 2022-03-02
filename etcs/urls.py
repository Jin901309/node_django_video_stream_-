from django .urls import path
from . import views

app_name="etcs"

urlpatterns = [
    path("ajax/like/<int:pk>/", views.LikeAjax.as_view(), name="like" ),
    path("likelist/", views.Likelist.as_view(), name="likelist" ),
    
    
    
]