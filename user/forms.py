from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ['username','password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            # self.add_error('username','this field is required')
            raise forms.ValidationError('this field is required')
        elif username not in [user.username for user in User.objects.all()]:
            raise forms.ValidationError('invalid username')
        else:
            return username


# class UserSignupForm(UserCreationForm):
