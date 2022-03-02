from django .urls import path
from . import views

app_name="channels"

urlpatterns = [
    path("<int:pk>/", views.MyChannel.as_view(), name="mychan" ),
    path("update-channel/", views.UpdateChannel.as_view(), name="update" ),
    
    
    
    
]