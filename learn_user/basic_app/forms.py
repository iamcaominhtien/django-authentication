from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='Mật khẩu')
    username = forms.CharField(label='Tên người dùng')
    email = forms.EmailField(label='Email')

    class Meta():
        model=User
        fields=('username','email','password')

class UserFrofileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')