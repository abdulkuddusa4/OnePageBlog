from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'bg-input text-success'
            }
        )

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'bg-input text-success'
            }
        )

    )

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


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-input text-success',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-input text-success',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-input text-success',
            }
        ),
        help_text= password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-input text-success'
            }
        )
    )
    class Meta:
        fields = ['username','email']
        model = User


