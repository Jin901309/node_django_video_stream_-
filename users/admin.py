from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationForm
from django.utils.translation import ngettext
from django.contrib import messages
# Register your models here.

@admin.action(description='선택된 사용자 을/를 활성화합니다.')
def change_activation(modeladmin, request, queryset):
    queryset.update(is_active=True)



@admin.action(description='선택된 사용자 을/를 비활성화합니다.')
def change_disabled(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='선택된 사용자 비밀번호 을/를 초기화합니다.')
def reset_password(modeladmin, request, queryset):
    for instance in queryset:
        instance.set_password('123456789a@')
        instance.save()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',  'is_admin', "is_active",
        "nickname",
        "login_method",
        
    )
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            "내정보",
            {
                "fields":(
                    "nickname",
                    "avatar",
                    "superhost",
                    
                )
            }
        ),
        
        ('주의하고 관리자 권한주십시오.', {'fields': ('is_active','is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2'),
        }),
    )
    actions = [change_activation, change_disabled, reset_password, ]
    search_fields = ('email','nickname',)
    # readonly_fields = ['password', ]
    ordering = ('email',)
    filter_horizontal = ()
    
    
    


admin.site.register(models.User, UserAdmin)
admin.site.unregister(Group)