from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class candidateLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'name': 'first_name','placeholder': 'First_Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'last_name','placeholder': 'Last_Name'}))
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'name': 'username','placeholder': 'UserName'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'name': 'password','placeholder': 'Password'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'name': 'email','placeholder': 'Email'}))
    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
    #                                 error_message=(
    #                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    #
class InstituteRegistrationForm(forms.Form):
    InstituteName = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'border-gradient', 'placeholder': 'Institute Name'}))
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'border-gradient', 'placeholder': 'UserName'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'border-gradient', 'placeholder': 'Password'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'border-gradient', 'placeholder': 'Email'}))

class InstituteLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))

class examDetails(forms.Form):
    examCode = forms.CharField(label="Exam Code", max_length=20,
                               widget=forms.TextInput(attrs={'name':'examCode', 'placeholder':'Exam code'}))
    examName = forms.CharField(label="Exam Name", max_length=20,
                               widget=forms.TextInput(attrs={'name': 'examName', 'placeholder': 'Exam name'}))
    totalTime = forms.TimeField(label="Total Time",widget=forms.TimeInput(format='%H:%M', attrs={'name':'totalTime', 'placeholder': '00:00'}))
    totalMark = forms.IntegerField(label="Total Marks",widget=forms.TextInput(attrs={'name':'totalTime', 'placeholder': 'Total Time'}))
    createdby = forms.CharField(label="UserName",widget=forms.TextInput(attrs={'name':'createdby', 'placeholder':'Your Username'}))