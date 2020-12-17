from django.conf.urls import url
from django.shortcuts import redirect
from . import views


urlpatterns = [
    url('^$',lambda request: redirect('posts'),name='home'),
    url('^posts/$',views.Posts.as_view(),name='posts'),
    url('^create-post/$',views.CreatePost.as_view(),name='post-create'),
]
