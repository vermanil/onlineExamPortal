from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import candidateLoginForm, RegistrationForm, InstituteLoginForm, InstituteRegistrationForm

# Create your views here.
def index(request):
    return render(request, "home.html", {})

def candidateLogin(request, name):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect("/")
        else:
            url = "/accounts/" + name + "/login"
            return HttpResponseRedirect(url)
    else:
        if name == "Candidate":
            form = candidateLoginForm()
        else:
            form = InstituteLoginForm()
        return render(request, "Login.html", {'form': form, "name": name})

def candidateRegister(request,name):
    print(request.method)
    print(name)
    if request.method == 'POST':
        if name=="Candidate":
            print("hello")
            form = RegistrationForm(request.POST)
        else:
            form = InstituteRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():  # invoke .is_valid
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            url="/accounts/" + name +"/login"
            print(url)
        return HttpResponseRedirect(url)
    else:
        if name=="Candidate":
            form = RegistrationForm()
        else:
            form = InstituteRegistrationForm()
        return render(request, "reg.html", {'form': form, "name": name})