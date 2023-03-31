from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

field_attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=field_attrs),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs=field_attrs),
    )


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=field_attrs),
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs=field_attrs),
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=field_attrs),
    )
    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(attrs=field_attrs),
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.TextInput(attrs=field_attrs),
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        strip=False,
        widget=forms.TextInput(attrs=field_attrs),
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs=field_attrs),
            'last_name': forms.TextInput(attrs=field_attrs),
            'email': forms.EmailInput(attrs=field_attrs),
        }
