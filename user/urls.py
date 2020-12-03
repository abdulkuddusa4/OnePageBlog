from . import views
from django.conf.urls import url


urlpatterns = [
    url('logout/$',views.Logout.as_view(),name='user-logout'),
    url('login/$',views.Login.as_view(),name='user-login'),
    url('create/$',views.CreateUser.as_view(),name='user-signup'),
]
