from . import views
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    url(r'logout/$',views.Logout.as_view(),name='user-logout'),
    url(r'login/$',views.Login.as_view(),name='user-login'),
    url(r'create/$',views.CreateUser.as_view(),name='user-signup'),
    url(r'verify/\\?next=(?P<url>\S*)?$',views.EmailVerify.as_view(),name='verify-email'),
    # url(r'verify/$',views.EmailVerify.as_view(),name='verify-email'),
]
