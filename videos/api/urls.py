from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('videos/', views.getVideos),
    path('videos/<str:pk>/', views.getVideo),
    
    
]
