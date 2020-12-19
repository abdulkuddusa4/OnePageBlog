"""OnePageBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from . import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render

# handler404 = lambda request,exception:render(request,"posts/404.html",{'exception':exception})
# handler400 = lambda request,exception:render(request,"posts/400.html",{'exception':exception})
# handler500 = lambda request,exception:render(request,"posts/500.html",{'exception':exception})

handler404 = lambda request,exception:HttpResponseNotFound('lol')
handler400 = lambda request,exception:HttpResponseNotFound('lol')
handler500 = lambda request,exception:HttpResponseNotFound('lol')


urlpatterns = [
    url('^admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('user/',include('user.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
