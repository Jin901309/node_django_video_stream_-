
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.translation import gettext_lazy as _
from django.shortcuts  import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname='admin',  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#PermissionsMixin 상속해야 모델 필드 추가할 수 있음 아님 추가안됨.
#관리자 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    LOGIN_EMAIL = "email"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGING_KAKAO, "Kakao"),
    )


    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
        null=True,
    )
    
    is_active = models.BooleanField(_("활성화권한"),default=True)
    is_admin = models.BooleanField(_("관리자권한"),default=False,)

    nickname=models.CharField(_("닉네임"),unique=True, max_length=25)

    # 사용자이미지
    avatar = models.ImageField(upload_to="avatars", verbose_name='사용자이미지', blank=True)
   
    # 프리미엄
    superhost = models.BooleanField(default=False, verbose_name='프리미엄')

    # 이메일 인증필드
    # e_secret = models.CharField(max_length=20, default="", blank=True)
    login_method=models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)
    


    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        # 데이터베이스에 저장할 이름
        db_table = 'user'
        # 관리자페이지에서 보여질 이름
        verbose_name = '사용자'
        # 복수
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        #사용자에게 특정 권한이 있습니까?
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        #사용자에게 `app_label` 앱을 볼 수 있는 권한이 있습니까?
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        return self.is_admin
    
    
    # def get_absolute_url(self):
    #     #자기 객체 자신을 보여주는 url이라 인자값이 필요함
    #     #관리자에서 해당 프로필 url을 볼수 있음
    #     #템플릿에서 바로 호출할수 있음
    #     return reverse('users:profile', kwargs={'pk': self.pk})