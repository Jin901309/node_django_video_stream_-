from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from core import mixins
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView

#카카오 로그인
import os
import requests
from django.core.files.base import ContentFile

#이메일 인증
from .models import User
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token
from django.template.loader import render_to_string
import threading


from django.views.generic.base import TemplateView
from . import forms, models
# Create your views here.


#쓰레드로 작업 쓰레드
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


#이메일 인증 동작 함수
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = '이메일 인증해서 계정활성화 해주세요.'
    email_body = render_to_string('users/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()



#로그인
class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name="users/login.html"
    form_class=forms.LoginForm
    
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse("core:home"))
        else:
            messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
            return redirect(reverse("core:home"))

    def get_success_url(self):
        next_url = self.request.GET.get("next=", None)
        
        if next_url is not None:
            return next_url
        else:
            return reverse("core:home")
        
        
# 회원가입
class SignUpView(mixins.LoggedOutOnlyView, SuccessMessageMixin, FormView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("core:home")
    success_message="회원가입이 완료되었어용~ 이메일 인증해주세요~"
    form_class = forms.SignUpForm
    initial = {
        "email":"cap9973@gmail.com",

    }

    def form_valid(self, form):
        form.save()
        # u.is_active=False
        # u.save()
        
        #회원가입시 로그인
        email = form.cleaned_data.get("email")

        # # secret = uuid.uuid4().hex[:20]
        # # self.e_secret = secret
        user=models.User.objects.get(email=email)
        
        
        send_activation_email(user, self.request)
        return super().form_valid(form)
    
#이메일 활성화 함수
def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_active= True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             '이메일인증이 완료 되었습니다. 로그인해주세요.')
        return redirect(reverse('users:login'))

    return render(request, 'users/activate-failed.html', {"user": user})

    
    
def log_out(request):
    
    logout(request)
    messages.info(request, f"로그아웃 되었습니다.")

    return redirect(reverse("core:home"))




def kakao_login(request):
    client_id=os.environ.get("KAKAO_KEY")
    redirect_uri="http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )

class KakaoException(Exception):
    pass

def kakao_callback(reqeust):
    try:
        
        client_id = os.environ.get("KAKAO_KEY")
        code=reqeust.GET.get('code', None)
        redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
        token_request=requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )

        token_json = token_request.json()
        error=token_json.get('error', None)
        if error is not None:
            raise KakaoException("인증 코드를 받을 수 없음")

        access_token=token_json.get("access_token")
        #정보요청
        api_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}",
            })
        profile_json=api_request.json()
        email=profile_json.get("kakao_account").get("email")
        if email is None:
            raise KakaoException("이메일을 입력해주세요.")
        
        properties=profile_json.get("kakao_account").get("profile")
        profile_image=properties.get('profile_image_url')
        profile_nickname=properties.get('nickname')
        print(properties.get('nickname'))
        try:
            user=User.objects.get(email=email)
            if user.login_method!=User.LOGING_KAKAO:
                raise  KakaoException(f"다음으로 로그인하십시오.: {user.login_method}")

        except User.DoesNotExist:
            user=User.objects.create(
                email=email,
                login_method=User.LOGING_KAKAO,
                is_active=True,
                nickname=profile_nickname,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request=requests.get(profile_image)
                user.avatar.save(f"{email}-avatar.jpg", ContentFile(photo_request.content))
           
                
       
        # messages.success(request._request, 'Success')
        login(reqeust, user)
        
        return redirect(reverse("core:home"))


    except KakaoException as e:
        messages.error(reqeust, e)
        return redirect(reverse("core:home"))
    
    
    
class UpdateProfileView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):        
    model=User
    template_name="users/update-profile.html"
    fields=(
        "avatar",
        "nickname",
        
    )
    success_url=reverse_lazy("core:home")
    success_message="프로필 업데이트 완료"
    #수정하고자하는 파일이 누구인지 pk값을 안받아와서
    def  get_object( self, queryset = None ): 
        #자기자신을 리턴
        return self.request.user
    
    #뷰안에서 사용되는 form의 인스턴스를 반환함
    #새로운 form도 생성이 가능
    def get_form(self, form_class=None):
        form= super().get_form(form_class=form_class)
        form.fields['nickname'].widget.attrs={'placeholder':'사용할 닉네임 입력'}
        return form
    
    
class UpdatePasswordView(mixins.LoggedInOnlyView, mixins.EmailLoginOnlyView, PasswordChangeView):
    template_name="users/update-password.html"
    
    
    
    def get_form(self, form_class=None):
        form= super().get_form(form_class=form_class)
        form.fields['old_password'].widget.attrs={'placeholder':'기존 패스워드 입력'}
        form.fields['new_password1'].widget.attrs={'placeholder':'새로운 패스워드 입력'}
        form.fields['new_password2'].widget.attrs={'placeholder':'새로운 패스워드 다시입력'}
        return form
    
    
    def get_success_url(self):
        #users:profile로 이동
        return self.request.user.get_absolute_url()
