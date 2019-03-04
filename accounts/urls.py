from django.conf.urls import url

from accounts.views import SignUp, login_view,login_user, logout_view


app_name = "accounts"

urlpatterns = [
    url(r'^register/$', SignUp.as_view(), name="signup"),
    url(r'^login/$', login_view, name="login"),
    url(r'^login_user/$', login_user, name="login_user"),
    url(r'^logout/$', logout_view, name="logout_view"),
]