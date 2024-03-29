from django.contrib.auth import login
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name = "users"

urlpatterns = [
    # 登陆页面
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
