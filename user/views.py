from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django import forms
from django import template

message_list = """
    {% if messages %}
        {% for message in messages %}
            <h3 class="alert alert-{{ message.tags }}" style="margin-bottom:1px">{{ message }}</h3>
        {% endfor %}
    {% endif %}
    
"""

class Login(View):
    def get(self,request):
        context = {
            'login_form': LoginForm(),
        }
        return render(request,'user/login-form.html',context)

    def post(self,request):
        form = LoginForm(request.POST)
        context = {
            'login_form': form
        }
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(request,username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None:
                login(request,user,)
                return HttpResponse("true")
            else:
                form.add_error('password',"password did'nt match")
                return render(request,'user/login-form.html',context)
            pass
        else:
            return render(request,'user/login-form.html',context)


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('posts')

    def post(self,request):
        logout(request)
        return redirect('posts')
    pass


class CreateUser(View):
    def get(self,request):
        context = {
            'signup_form': UserCreationForm(),
        }
        return render(request,'user/signup-form.html',context)

    def post(self,request):
        form = UserCreationForm(request.POST)
        context = {
            'signup_form':form,
        }
        print('******debug')
        print(request.POST['username'])
        print(request.POST['password1'])
        print(request.POST['password2'])
        print('******debug')
        if form.is_valid():
            print('true..........')
            # form.save()
            messages.success(request,"account created successfully.")

            # return redirect('posts')
            return HttpResponse('1')
        else:
            print('false')
            print(form.error_messages)
            return render(request,'user/signup-form.html',context)
            # return render(request,'user/signup-form.html',context)
        pass

