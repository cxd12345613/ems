from django.urls import path
from  security_app import views

app_name='secu'

urlpatterns=[
        path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
]