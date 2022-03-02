from django.urls import path
from videos import views 
from . import views


app_name="reviews"


urlpatterns = [
    path("edit/", views.EditView.as_view(), name="edit"),
    path("delete/<int:pk>", views.DeleteView.as_view(), name="del"),
    
   
    
    
    
]

