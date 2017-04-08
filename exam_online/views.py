from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import exam_details, questionDetails, optionDetail, scores
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
            # print(user.is_staff)
            if name == "Institute":
                login(request, user)
                url = "/" + name + "/exam"
                return HttpResponseRedirect(url)
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
    return render(request, "exam_details.html", {'name':name, 'listCode':AllExamCode, 'user':request.user})

# @login_required(login_url='/')
# def setPaper(request, name):
#     # print(name)
#     l = ["qwer","asdfg","sxqaezd","qazbb"]
#     return render(request, "setExamCode.html", {'name':name,"l":l})

@login_required(login_url='/')
def startExam(request,name):
    print(name)
    # if exam_details.objects.get(request.examCode):
    #     wrong = "true"
    # else:
    #     wrong = "wrong"
    return render(request, "selectCode.html", {'name':name,'wrong':"true"})

@login_required(login_url='/')
def setEditQues(request, name):
    examCode = exam_details.objects.filter(createdby=request.user)
    return render(request,'listAllExamCode.html',{'name':name,'examCode':examCode})

# @login_required(login_url='/')
# def questionForm(request, name):
#     return render(request, "questionForm.html", {})
@login_required(login_url='/')
def setQues(request, name):
    if request.method == "POST":
        examCode = request.POST['examCode']
        return render(request, "setQuesPaper.html", {'name':name,'examCode':examCode})

@login_required(login_url='/')
def sessionStart(request, name):
    if request.method == "POST":
        code = request.POST['examCode']
        print(code)
        total_time = exam_details.objects.filter(examCode=code)
        print(total_time.values())
        allQuestion = optionDetail.objects.filter(code=code)
        # print(q_id.values())
        ques = []
        for i in allQuestion.values():
            ques.append(i['q_id'])
            # print(i['question_id'])
            # allQuestion = optionDetail.objects.filter(q_id=i['question_id'])
            # print(allQuestion.values())
        return render(request, "showQuestion.html", {'allQuestion':allQuestion,'examCode':code, 'tot':ques,'total':total_time})

@login_required(login_url='/')
def editQuestionForm(request, name,code):
    print(code)
    allQuestion = optionDetail.objects.filter(code=code)
    print(allQuestion.values())
    # for i in q_id.values():
    #     # print(i['question_id'])
    #     allQuestion = optionDetail.objects.filter(q_id=i['question_id'])
    #     print(allQuestion.values())
    return render(request, "editQuestion.html", {'allQuestion':allQuestion, 'examCode': code,'name':name})

@login_required(login_url='/')
def CandidateScore(request, name):
    examCode = exam_details.objects.filter(createdby=request.user)
    return render(request, 'candidateScore.html', {'name': name, 'examCode': examCode})

@login_required(login_url='/')
def selectExamCode(request, name):
    user = request.user
    user = scores.objects.filter(user=user)
    # print(user.values())
    return render(request,'candidateRank.html', {'name':name,'user':user})

@login_required(login_url='/')
def showListBoard(request, name):
    score = scores.objects.filter(examCode=request.POST['examCode']).order_by('rank')
    print(score.count())
    if score.count() == 0:
        return render(request,'leaderBoard_all.html', {'name':name,'score':score,'None':"True"})
    else:
        return render(request,'leaderBoard_all.html', {'name':name,'score':score,'None':"False"})

@login_required(login_url='/')
def seeLeaderboard(request, name):
    if request.method == "POST":
        examCode = request.POST['examCode']
        user = request.user
        user = scores.objects.filter(user=user)
        if user.count() == 0:
            none = "True"
        else:
            print(examCode)
            none="False"
            return render(request,'leaderBoard.html', {'name':name,'examCode':examCode,'user':user,'none':none})


@login_required(login_url='/')
def submitQuestion(request, name):
    if request.method == "POST":
        o = exam_details.objects.filter(examCode=request.POST['examCode'])
        if o.count() == 0:
            status = 0
            return HttpResponse(status)
        else:
            o = exam_details.objects.filter(examCode=request.POST['quesNum'])
            if o.count() == 0:
                Code = request.POST['examCode']
                number = request.POST['quesNum']
                question = request.POST['quest']
                mark = request.POST['questMark']
                option1 = request.POST['opt1']
                option2 = request.POST['opt2']
                option3 = request.POST['opt3']
                option4 = request.POST['opt4']
                correct = request.POST['correct']
                questDetails = questionDetails(code=Code, question_id=number)
                questDetails.save()
                optDetails = optionDetail(code=Code,q_id=number,question=question,questionMark=mark,option1=option1,option2=option2,option3=option3,option4=option4,correctAnswer=correct)
                optDetails.save()
                o = exam_details.objects.get(examCode=request.POST['examCode'])
                o.totalMark = o.totalMark + int(mark)
                o.save()
                return render(request,'setQuesPaper.html', {'name':name,'examCode':Code})
            else:
                status = 0
                return HttpResponse(status)

@login_required(login_url='/')
def updateQues(request, name):
    if request.method == "POST":
        # o = exam_details.objects.filter(examCode=request.POST['examCode'])
        # if o.count() == 0:
        #     status = 0
        #     return HttpResponse(status)
        o = exam_details.objects.filter(examCode=request.POST['quesNum'])
        if o.count() == 0:
            Code = request.POST['examCode']
            number = request.POST['quesNum']
            question = request.POST['quest']
            mark = request.POST['questMark']
            option1 = request.POST['opt1']
            option2 = request.POST['opt2']
            option3 = request.POST['opt3']
            option4 = request.POST['opt4']
            correct = request.POST['correct']
            questDetails = questionDetails(code=Code, question_id=number)
            questDetails.save()
            update = optionDetail.objects.get(code=Code,q_id=number)
            update.code = Code
            update.q_id = number
            update.question = question
            if update.questionMark != mark:
                o = exam_details.objects.get(examCode=request.POST['examCode'])
                o.totalMark = o.totalMark + int(mark) - update.questionMark
                o.save()
            update.questionMark = mark
            update.option1 = option1
            update.option2 = option2
            update.option3 = option3
            update.option4 = option4
            update.correctAnswer = correct
            update.save()
            return render(request,'setQuesPaper.html', {'name':name,'examCode':Code})
        else:
            status = 0
            return HttpResponse(status)


@login_required(login_url='/')
def submitExDetail(request, name):
    if request.method == "POST":
        # print(request.user)
        o = exam_details.objects.filter(examCode=request.POST['examCode'])
        # print(o.count())
        if(o.count() == 0):
            c = request.POST['createdBy']
            if str(request.user) == str(c):
                Code = request.POST['examCode']
                Name = request.POST['examName']
                Time = request.POST['totalTime']
                Mark = 0
                created = request.POST['createdBy']
                detail = exam_details(examCode = Code,examName=Name,totalTime=Time, totalMark=Mark,createdby=created)
                detail.save()
                print(Code)
                status = 1
                return HttpResponse(status)
            else:
                status = 0
                return HttpResponse(status)
        else:
            status = 0
            return HttpResponse(status)

@login_required(login_url='/')
def finalScore(request, name):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("You have submitted the score")

