from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

class EmailLoginOnlyView(UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.login_method=="email"
    
    def handle_no_permission(self):
        messages.error(self.request, "해당페이지로 이동 할수 없습니다.")
        return redirect("core:home")
    
 #로그인 한사람이 로그인 페이지를 입력해서 가는걸 막는 뷰
class LoggedOutOnlyView(UserPassesTestMixin):
    
    permission_denied_message="페이지 에러404"
    
    def test_func(self):
        #ture 값은 유저는 인증이 되지않았음을 의미(익명의유저)
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        messages.error(self.request, "해당페이지로 이동 할수 없습니다.")
        return redirect("core:home")   
    
    
#해당페이지를 이동할때 로그인이 안되있으면 로그인 페이지로 이동하게 해주는 뷰
class LoggedInOnlyView(LoginRequiredMixin):
    login_url=reverse_lazy("users:login")
    
    

    