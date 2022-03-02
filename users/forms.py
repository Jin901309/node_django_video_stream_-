from django import forms
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.hashers import check_password
from .models import User



styles='width:100%;  margin-bottom:5px; border-bottom:solid 1px rgba(0, 0, 255, .2); padding: 10px; font-size: 18px;'



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='패스워드', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='패스워드 확인', widget=forms.PasswordInput)
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('이메일'),
                'required': 'True',
            }
        )
    )
    nickname=forms.CharField(
        label=_('닉네임'),
        required=True,
        
        widget=forms.TextInput(
            attrs={
                'placeholder':_('닉네임'),
                'required':'True',
            }
        )
    )
    class Meta:
        model = User
        fields = ('email','nickname',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("패스워드가 서로 일치하지 않음")
        validate_password(password2)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
                                                "이 사용자의 암호를 직접볼순 없습니다. "
                                                "패스워드를 변경할려면  <a href=\"%s\"> "
                                                "<strong>이곳을 눌러주십시오.</strong></a>"
                                            ) % reverse_lazy('admin:auth_user_password_change', args=[self.instance.id])
        self.fields['password'].label=("패스워드")


    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
    
    
    
class LoginForm(forms.Form):
    email=forms.EmailField(label="이메일",  widget=forms.EmailInput(attrs={
        'placeholder': '이메일 입력',
        'style': 'width:100%;  margin-bottom:5px; border-bottom:solid 1px rgba(0, 0, 255, .2); padding: 10px; font-size: 18px;'
        }))
    password=forms.CharField(label="패스워드",  widget=forms.PasswordInput(attrs={
        'placeholder': '패스워드 입력',
        'style': 'width:100%; margin-bottom:5px;margin-bottom:5px; border-bottom:solid 1px rgba(0, 0, 255, .2); padding: 10px; font-size: 18px;'
        }))

    def clean(self):
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        try:
            user=User.objects.get(email=email)
            
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드가 일치하지 않습니다."))

        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError("사용자가 존재하지 않습니다."))


class SignUpForm(forms.ModelForm):
    
    class Meta:
        
        model=User
        fields=['email', 'nickname',]
        widgets={
            'email':forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('이메일'),
                'required': 'True',
                'style': f'{styles}',
            }
            ),
            'nickname':forms.TextInput(
                attrs={
                    'placeholder':_('닉네임'),
                    'style': f'{styles}',
                }
            )
        }
        
    password = forms.CharField(label="비밀번호",widget=forms.PasswordInput(attrs={
        'placeholder': '패스워드 입력',
        'style': f'{styles}',
        }))
    password1 = forms.CharField(label="비밀번호 재입력",widget=forms.PasswordInput(attrs={
        'placeholder': '패스워드 확인',
        'style': f'{styles}',
        }))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
                raise forms.ValidationError("패스워드가 일치하지않습니다.")
        validate_password(password)
        return password

    def save(self, *args, **kwargs):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.is_active=False
        user.save()  # commit=True
        
        

   
        
# class Signup(SignupForm):
#     nickname = forms.CharField(max_length=30, label='nickname')

#     def save(self, request):
    
#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(Signup, self).save(request)


#         user.nickname=self.cleaned_data.get("nickname")
#         user.save()

#         # You must return the original result.
#         return user

#     # def signup(self, request, user):
#     #     user.nickname = self.cleaned_data['nickname']
        
#     #     user.save()
#     #     return user
    
    