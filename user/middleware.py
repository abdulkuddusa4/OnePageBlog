from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.shortcuts import render,redirect,resolve_url
from django.urls import resolve
from user.views import EmailVerify
from django.contrib import messages
from django import template


def redirect_from_middleware(request,url_name,get_response):
    print('debug',request.path)
    if resolve_url(url_name) not in request.path:
        return redirect(url_name,url=request.path)
    else:
        ...
        return get_response(request)


class EmailValidationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        pass
    def __call__(self, request,*args, **kwargs):
        user = request.user
        if resolve(request.path).url_name == 'user-login' or resolve(request.path).url_name =='user-logout':
            return self.get_response(request)

        else:
            if not user.is_anonymous and user.email and not user.emailvalidator.is_validate:
                return redirect_from_middleware(request,'verify-email', self.get_response)
            else:
                return self.get_response(request)
