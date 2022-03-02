from django .urls import path
from . import views

app_name="users"

urlpatterns = [
    
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('login/kakao', views.kakao_login, name="kakao-login"),
    path('login/kakao/callback/', views.kakao_callback, name="kakao-callback"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),  
]