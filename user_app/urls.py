from django.urls import path
from user_app import views
app_name='user_app'

urlpatterns=[

    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='regisrlogic'),
    path('checkName/',views.checkName,name='checkName'),
    path('checkCaptcha/',views.checkCaptcha,name='checkCaptcha'),


]