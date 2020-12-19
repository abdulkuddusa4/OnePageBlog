from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .forms import UserSignupForm as UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.core.mail import send_mail
from django import template
from random import randint as ri
from OnePageBlog import settings
from django.contrib.auth.models import User
NEXT_URL = None
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
            user=authenticate(request,username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None:
                    # error_message = 'the email you provide with this account was not varified.please <a href={% url "verify-email" %} style="color:red;">click here</a> to varify your email account.'
                    # my_t = template.Template(error_message).render(template.RequestContext(request))

                    # messages.error(request,my_t,extra_tags='danger')
                login(request,user)
                return HttpResponse('true')
            else:
                form.add_error('password',"invalid password")
                return render(request,'user/login-form.html',context)
            pass
        else:
            return render(request,'user/login-form.html',context)


class Logout(View):
    def get(self,request):
        print('debug_logout',request.path)
        logout(request)
        return redirect('posts')

    def post(self,request):
        pass
    pass


class CreateUser(View):
    def get(self,request):
        context = {
            'signup_form': UserCreationForm(),
        }
        return render(request,'user/signup-form.html',context)

    def post(self,request):
        form = UserCreationForm(request.POST)
        print('ddd')
        print(request.POST)
        print('ddd')
        context = {
            'signup_form':form,
        }
        if form.is_valid():
            print('true..........')
            print(form.cleaned_data.get('email'))
            form.save()
            messages.success(request,"account created successfully.")

            # return redirect('posts')
            return HttpResponse('1')
        else:
            print('false')
            print(form.error_messages)
            return render(request,'user/signup-form.html',context)
            # return render(request,'user/signup-form.html',context)
        pass


class EmailVerify(View):
    def get(self,request,url=None,msg=None):


        global NEXT_URL
        if url is not None:
            NEXT_URL = url
            pass
        if 'from_redirect_itself' not in request.session.keys():
            request.session['from_redirect_itself'] = False
        print('debug__*******')
        print((request.session['from_redirect_itself']))
        print('debug__*******')
        if request.session['from_redirect_itself'] is True:
            request.session.pop('from_redirect_itself')
            return render(request,'user/email-verification-page.html',{'msg':'invalid code'})
        else:

            if not request.user.is_anonymous:
                if request.user.email:
                    if not request.user.emailvalidator.is_validate:
                        message = 'the email you provide with this account was not verified.First, please verify your email with the verification code we have send to <strong>{{ user.email }} </strong>in decimal number.'
                        verification_code = ''.join(map(str,(ri(0,9),ri(0,9),ri(0,9),ri(0,9),ri(0,9),ri(0,9))))
                        request.session['verification_code'] = verification_code
                        msg = f'your email verification code is {verification_code}'
                        send_mail('verification code from onepageblog', msg,settings.EMAIL_HOST_USER,[request.user.email])
                        my_t = template.Template(message).render(template.RequestContext(request))
                        messages.success(request,my_t,)
                        return render(request,'user/email-verification-page.html')
                    else:
                        messages.success(request,'the email with this account was already verified')
                        return redirect(NEXT_URL) if NEXT_URL else redirect('posts')
                else:
                    message = "no email was attached with this account for email-verification"
                    messages.success(request,message)
                    if NEXT_URL:
                        return redirect(NEXT_URL)
                    else:
                        return redirect('/')
            else:
                messages.success(request,'Sir, we need a logged in account for email-verification of that account')
                if NEXT_URL:
                    return redirect(NEXT_URL)
                else:
                    return redirect('posts')

    def post(self,request,url=None):
        # if 'email_verification_code' in request.session.keys():

            print('haha url',url)
            code = request.POST['email_verification_code']
            print(code)
            print(request.session['verification_code'])
            if request.session['verification_code'] == code:
                validationmodel = User.objects.get(username=request.user.username).emailvalidator
                validationmodel.is_validate = True
                validationmodel.save()
                request.session.pop('verification_code')
                messages.success(request,'verification completed')
                if NEXT_URL:
                    return redirect(NEXT_URL)
                else:
                    return redirect('posts')
            else:
                request.session['from_redirect_itself'] = True
                # response =  render(request, 'user/email-verification-page.html', {'msg': 'invalid code'})
                # print('debug_*******')
                # response['Location'] = 'haha'
                # response.url = property(lambda response: response['Location'])
                # print(response['Location'])
                # print('debug_*******')
                return redirect('verify-email',url=NEXT_URL)
        # else:
        #     messages.success(request,'there is a n error. Maybe the session for this code has expired. Plese verify again with another code we have sent')
        #     return redirect('verify-email',url=NEXT_URL)
