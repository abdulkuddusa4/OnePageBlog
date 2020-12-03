from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django import template
from django.contrib import messages
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form
from time import sleep


class Posts(View):
    def get(self,request):
        context = {
            'posts': Post.objects.all(),
            'form': PostForm(),
        }

        return render(request,'posts/posts.html',context)


class CreatePost(View):
    def get(self,request):
        form = PostForm()
        form = template.Template(as_crispy_form(form)).render(template.RequestContext(request))
        context = {
            'add_post_form':form,
        }
        sleep(1)
        return render(request,'posts/AddPostForm.html',context)
        pass

    def post(self,request):
        form = PostForm(request.POST)
        # print('***************')
        # print(request.POST.dict)
        # print(form.is_valid())
        # print(form.is_valid())
        # print('***************')
        if form.is_valid():
        #     print(form.is_bound)
            print("********debug******")
            form.save()
            messages.success(request,"post created")
            add_post_form = template.Template(as_crispy_form(PostForm())).render(template.RequestContext(request))
            return render(request,'posts/AddPostForm.html',{'add_post_form':add_post_form})
        #
        else:
            print('error_block')
            form = template.Template(as_crispy_form(form)).render(template.RequestContext(request))
            return render(request,'posts/AddPostForm.html',{'add_post_form':form})
            add_post_form = template.Template(as_crispy_form(PostForm())).render(template.RequestContext(request))
            return render(request,'posts/AddPostForm.html',{'add_post_form':add_post_form})
