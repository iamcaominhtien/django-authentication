from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('dang-ki/',views.registration,name='dang-ki'),
    path('dang-nhap/',views.user_login,name='dang-nhap'),
]