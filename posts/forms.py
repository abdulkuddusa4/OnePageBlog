from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    author = forms.CharField(
        max_length=12,
        widget=forms.HiddenInput(
            attrs={
                'value':'{{ user.id }}',
            }
        ),
        required=True
    )
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'please provide a meaningful title',
                'class':'bg-input text-success',
            },
        )
    )

    short_description = forms.CharField(
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'class':'bg-input text-success'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '5',
                'class': 'bg-input text-success'
            }
        ),
    )

    class Meta:
        model = Post
        fields = ['author','title','short_description','description',]

    def clean_author(self):
        print(self.data.get('author'))
        user = User.objects.get(id=self.data.get('author'))
        return user

    def clean_title(self):
        if self.data.get('title').strip() is '':
            raise forms.ValidationError('this field is required')
        else:
            return self.data.get('title')
