from django.urls import path
from videos import views 
from . import views as view_search


app_name="core"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("search/", view_search.resolve_search, name="search"),
    
    
    
]

