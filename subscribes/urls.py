from django .urls import path
from . import views




app_name="sub"

urlpatterns = [
    path("sublist/", views.SubList.as_view(), name="sublist" ),
    path("<int:pk>/", views.Subplus.as_view(), name="edit" ),
   
    
    
    
]