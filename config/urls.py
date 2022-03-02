"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import redirect


# def protected_file(request, path, document_root=None):
#     messages.error(request, "접근 불가")
#     return redirect('/')


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('users/', include('users.urls', namespace='users')),
    path('videos/', include('videos.urls', namespace='videos')),
    path('etcs/', include('etcs.urls', namespace='etcs')),
    path('sub/', include('subscribes.urls', namespace='sub')),
    path('channel/', include('channels.urls', namespace='channels')),
    path('review/', include('reviews.urls', namespace='reviews')),
    path('api/', include('videos.api.urls')),
    
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon/favicon.ico')),
    # path('accounts/', include('allauth.urls')),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
    