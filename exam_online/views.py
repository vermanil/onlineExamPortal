from django.shortcuts import render
from django.http import HttpResponse
from .forms import candidateLoginForm, RegistrationForm, InstituteLoginForm, InstituteRegistrationForm

# Create your views here.
def index(request):
    return render(request, "home.html", {})

def candidateLogin(request, name):
    if name == "Candidate":
        form = candidateLoginForm()
    else:
        form = InstituteLoginForm()
    return render(request, "Login.html", {'form': form, "name": name})

def candidateRegister(request,name):
    if name=="Candidate":
        form = RegistrationForm()
    else:
        form = InstituteRegistrationForm()
    return render(request, "reg.html", {'form1': form, "name": name})