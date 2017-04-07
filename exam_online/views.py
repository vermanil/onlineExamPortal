from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import exam_details
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import candidateLoginForm, RegistrationForm, InstituteLoginForm, InstituteRegistrationForm\
    # , examDetails

# Create your views here.
def index(request):
    return render(request, "home.html", {})

def candidateLogin(request, name):
    if request.method == 'POST':
        print(name)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user.is_staff)
            if name == "Institute":
                login(request, user)
                # print(name)
                url = "/" + name + "/exam"
                # print(url)
                return HttpResponseRedirect(url)
            # else:
            #     url = "/accounts/" + name + "/login"
            #     return HttpResponseRedirect(url)
            # if name == "Candidate":
            #     print(name)
            elif name == "Candidate":
                print(name)
                login(request, user)
                # print(name)
                url = "/" + name + "/exam"
                # print(url)
                return HttpResponseRedirect(url)
            else:
                url = "/accounts/" + name + "/login"
                return HttpResponseRedirect(url)
        else:
            url = "/accounts/" + name + "/login"
            return HttpResponseRedirect(url)
    else:
        if name == "Candidate":
            form = candidateLoginForm()
        else:
            form = InstituteLoginForm()
        return render(request, "Login.html", {'form': form, "name": name})

@login_required(login_url='/')
def Clogout(request,name):
    logout(request)
    if name=="Candidate":
        url= "/accounts/" + name + "/login"
    else:
        url = "/accounts/" + name + "/login"
    return HttpResponseRedirect(url)

def candidateRegister(request,name):
    # print(request.method)
    # print(name)
    if request.method == 'POST':
        if name=="Candidate":
            # print("hello")
            form = RegistrationForm(request.POST)
        else:
            form = InstituteRegistrationForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():  # invoke .is_valid
            if name == "Candidate":
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                # print(url)
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    is_staff=True
                )
                user.name = form.cleaned_data['InstituteName']
            user.save()
            url = "/accounts/" + name + "/login"
        return HttpResponseRedirect(url)
    else:
        if name=="Candidate":
            form = RegistrationForm()
        else:
            form = InstituteRegistrationForm()
        return render(request, "reg.html", {'form': form, "name": name})

@login_required(login_url='/')
def exam(request, name):
    print(request.user)
    user = request.user
    if name == "Institute":
        return render(request,'institutePortal.html',{'name':name,'user':user})
    else:
        return render(request, 'candidatePortal.html', {'name': name,'user':user})

@login_required(login_url='/')
def aboutExam(request, name):
    print("hello")
    # form = examDetails()
    AllExamCode = "none"
    return render(request, "exam_details.html", {'name':name, 'listCode':AllExamCode})

# @login_required(login_url='/')
# def setPaper(request, name):
#     # print(name)
#     l = ["qwer","asdfg","sxqaezd","qazbb"]
#     return render(request, "setExamCode.html", {'name':name,"l":l})

# @login_required(login_url='/')
# def startExam(request,name):
#     print(name)
#     # if exam_details.objects.get(request.examCode):
#     #     wrong = "true"
#     # else:
#     #     wrong = "wrong"
#     return render(request, "candidateExam.html", {'name':name,'wrong':"true"})

@login_required(login_url='/')
def setEditQues(request, name):
    return render(request,'setQuesPaper.html',{'name':name})

# @login_required(login_url='/')
# def questionForm(request, name):
#     return render(request, "questionForm.html", {})

@login_required(login_url='/')
def editQuestionForm(request, name):
    return render(request, "editQuestion.html", {})

@login_required(login_url='/')
def CandidateScore(request, name):
    return render(request,'candidateScore.html', {'name':name})
