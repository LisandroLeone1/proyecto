from django.urls import path
from core.views import index, CustomLoginViews, register
from django.contrib.auth.views import LogoutView

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginViews.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name = "core/logout.html"), name="logout"),
    path("register/",register,name="register")
]