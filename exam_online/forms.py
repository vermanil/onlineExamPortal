from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class candidateLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))


class RegistrationForm(AuthenticationForm):
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'border-gradient', 'placeholder': 'First_Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'border-gradient', 'placeholder': 'Last_Name'}))
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'border-gradient', 'placeholder': 'UserName'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'border-gradient', 'placeholder': 'Password'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'border-gradient', 'placeholder': 'Email'}))
    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
    #                                 error_message=(
    #                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    #
class InstituteRegistrationForm(AuthenticationForm):
    InstituteName = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'border-gradient', 'placeholder': 'Institute Name'}))
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'border-gradient', 'placeholder': 'UserName'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'border-gradient', 'placeholder': 'Password'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'border-gradient', 'placeholder': 'Email'}))

class InstituteLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))