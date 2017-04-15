from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import exam_details, questionDetails, optionDetail, scores, timeManager
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import candidateLoginForm, RegistrationForm, InstituteLoginForm, InstituteRegistrationForm
from django.utils import timezone


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
            # print(name)
            if name == "Institute" and user.is_staff:
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
                status = "User does not exist"
                if name == "Candidate":
                    form = candidateLoginForm()
                else:
                    form = InstituteLoginForm()
                return render(request, "Login.html", {'form': form, "name": name, 'status': status})
        else:
            url = "/accounts/" + name + "/login"
            status = 0
            if name == "Candidate":
                form = candidateLoginForm()
            else:
                form = InstituteLoginForm()
            return render(request, "Login.html", {'form': form, "name": name, 'status': status})
    else:
        status = 1
        if name == "Candidate":
            form = candidateLoginForm()
        else:
            form = InstituteLoginForm()
        return render(request, "Login.html", {'form': form, "name": name, 'status': status})


@login_required(login_url='/')
def Clogout(request, name):
    logout(request)
    if name == "Candidate":
        url = "/accounts/" + name + "/login"
    else:
        url = "/accounts/" + name + "/login"
    return HttpResponseRedirect(url)


def candidateRegister(request, name):
    # print(request.method)
    # print(name)
    if request.method == 'POST':
        if name == "Candidate":
            # print("hello")
            form = RegistrationForm(request.POST)
        else:
            form = InstituteRegistrationForm(request.POST)

        if form.is_valid():  # invoke .is_valid
            if name == "Candidate":
                username = form.cleaned_data['username']
                alreadyUser = User.objects.filter(username=username)
                # print(alreadyUser.count())
                if (alreadyUser.count() != 0):
                    form = RegistrationForm()
                    return render(request, "reg.html", {'form': form, "name": name, 'stat': "User already exist"})
                else:
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password']
                    )
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.save()
                    form = candidateLoginForm()
                    return render(request, "Login.html", {'form': form, "name": name})
                    # print(url)
            elif name == "Institute":
                username = form.cleaned_data['username']
                alreadyUser = User.objects.filter(username=username)
                # print(alreadyUser.count())
                if (alreadyUser.count() != 0):
                    form = InstituteRegistrationForm()
                    return render(request, "reg.html", {'form': form, "name": name, 'stat': "User already exist"})
                else:
                    print("hello")
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        is_staff=True
                    )
                    user.name = form.cleaned_data['InstituteName']
                    user.save()
                    form = InstituteLoginForm()
                    return render(request, "Login.html", {'form': form, "name": name})
            else:
                status = 3
            status = 2
            # url = "/accounts/" + name + "/login"
            return render(request, "Login.html", {'form': form, "name": name, 'status': status})
    else:
        if name == "Candidate":
            form = RegistrationForm()
            status = 1
        elif name == "Institute":
            form = InstituteRegistrationForm()
            status = 1
        else:
            status = 3
            return render(request, "reg.html", {"name": name, 'status': status})
        return render(request, "reg.html", {'form': form, "name": name, 'status': status})


@login_required(login_url='/')
def exam(request, name):
    print(request.user)
    user = request.user
    if name == "Institute":
        return render(request, 'institutePortal.html', {'name': name, 'user': user})
    else:
        return render(request, 'candidatePortal.html', {'name': name, 'user': user})


@login_required(login_url='/')
def aboutExam(request, name):
    print("hello")
    # form = examDetails()
    AllExamCode = "none"
    return render(request, "exam_details.html", {'name': name, 'listCode': AllExamCode, 'user': request.user})


# @login_required(login_url='/')
# def setPaper(request, name):
#     # print(name)
#     l = ["qwer","asdfg","sxqaezd","qazbb"]
#     return render(request, "setExamCode.html", {'name':name,"l":l})

@login_required(login_url='/')
def startExam(request, name):
    print(name)
    # if exam_details.objects.get(request.examCode):
    #     wrong = "true"
    # else:
    #     wrong = "wrong"
    return render(request, "selectCode.html", {'name': name, 'wrong': "false"})


@login_required(login_url='/')
def setEditQues(request, name):
    examCode = exam_details.objects.filter(createdby=request.user)
    return render(request, 'listAllExamCode.html', {'name': name, 'examCode': examCode, "noQues": "yes"})


# @login_required(login_url='/')
# def questionForm(request, name):
#     return render(request, "questionForm.html", {})
@login_required(login_url='/')
def setQues(request, name):
    if request.method == "POST":
        examCode = request.POST['examCode']
        return render(request, "setQuesPaper.html", {'name': name, 'examCode': examCode})


@login_required(login_url='/')
def sessionStart(request, name):
    if request.method == "POST":
        code = request.POST['examCode']
        print(code)
        total_time = exam_details.objects.filter(examCode=code)
        print(total_time.values())
        allQuestion = optionDetail.objects.filter(code=code)
        totalQuest = allQuestion.count()
        if allQuestion.count() != 0:
            # print(q_id.values())
            ques = []
            for i in allQuestion.values():
                ques.append(i['q_id'])
            return render(request, "showQuestion.html",
                          {'allQuestion': allQuestion, 'examCode': code, 'tot': ques, 'total': total_time,
                           'totalQuest': totalQuest})
        else:
            return render(request, "selectCode.html", {'name': name, 'wrong': "true"})


def timeManage(request, name):
    print(request.user)
    tim = timeManager.objects.filter(user=request.user)
    if tim.count() != 0:
        time = timeManager.objects.get(user=request.user)
        # print(time.user)
        # print(request.user)
        # if str(time.user) == str(request.user):
        time.startTime = timezone.now()
        time.save()
        data = 1
    else:
        tim = timeManager(user=request.user)
        tim.save()
        data = 1
    return HttpResponse(data)


@login_required(login_url='/')
def editQuestionForm(request, name, code):
    print(code)
    allQuestion = optionDetail.objects.filter(code=code)
    l = allQuestion.count()
    # for i in q_id.values():
    #     # print(i['question_id'])
    #     allQuestion = optionDetail.objects.filter(q_id=i['question_id'])
    #     print(allQuestion.values())
    if allQuestion.count() != 0:
        return render(request, "editQuestion.html",
                      {'allQuestion': allQuestion, 'examCode': code, 'name': name, "len": l})
    else:
        examCode = exam_details.objects.filter(createdby=request.user)
        return render(request, 'listAllExamCode.html', {'name': name, 'examCode': examCode, "noQues": "NoQuestion", })


@login_required(login_url='/')
def CandidateScore(request, name):
    examCode = exam_details.objects.filter(createdby=request.user)
    return render(request, 'candidateScore.html', {'name': name, 'examCode': examCode})


@login_required(login_url='/')
def selectExamCode(request, name):
    user = request.user
    user = scores.objects.filter(user=user)
    c = user.count()
    # print(user.values())
    user = list(user.values())
    result = {}
    for i in range(0, c):
        # print(user[i])
        for key, value in user[i].items():
            if value not in result.values():
                result[key] = value
    user = []
    user.append(result)
    # print(user)
    if c != 0:
        return render(request, 'candidateRank.html', {'name': name, 'user': user, 'givenExam': "Yes"})
    else:
        return render(request, 'candidateRank.html', {'name': name, 'user': user, 'givenExam': "no"})


@login_required(login_url='/')
def showListBoard(request, name):
    score = scores.objects.filter(examCode=request.POST['examCode']).order_by('-score')
    print(score.count())
    if score.count() == 0:
        return render(request, 'leaderBoard_all.html', {'name': name, 'score': score, 'None': "True"})
    else:
        return render(request, 'leaderBoard_all.html', {'name': name, 'score': score, 'None': "False"})


@login_required(login_url='/')
def seeLeaderboard(request, name):
    if request.method == "POST":
        examCode = request.POST['examCode']
        user = request.user
        user = scores.objects.filter(examCode=examCode)
        if user.count() == 0:
            none = "True"
            return render(request, 'leaderBoard.html', {'name': name, 'examCode': examCode, 'user': user, 'none': none})
        else:
            print(examCode)
            none = "False"
            return render(request, 'leaderBoard.html', {'name': name, 'examCode': examCode, 'user': user, 'none': none})


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
                optDetails = optionDetail(code=Code, q_id=number, question=question, questionMark=mark, option1=option1,
                                          option2=option2, option3=option3, option4=option4, correctAnswer=correct)
                optDetails.save()
                o = exam_details.objects.get(examCode=request.POST['examCode'])
                o.totalMark = o.totalMark + int(mark)
                o.save()
                return render(request, 'setQuesPaper.html', {'name': name, 'examCode': Code})
            else:
                status = 0
                return HttpResponse(status)


@login_required(login_url='/')
def updateQues(request, name):
    if request.method == "POST":
        o = exam_details.objects.filter(examCode=request.POST['quesNum'])
        print(o.count())
        if o.count() == 0:
            Code = request.POST['examCode']
            number = request.POST['quesNum']
            question = request.POST['quest']
            mark = request.POST['questMark']
            option1 = request.POST['opt1']
            print(option1)
            option2 = request.POST['opt2']
            option3 = request.POST['opt3']
            option4 = request.POST['opt4']
            correct = request.POST['correct']
            # questDetails = questionDetails(code=Code, question_id=number)
            # questDetails.save()
            update = optionDetail.objects.get(code=Code, q_id=number)
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
            return render(request, 'setQuesPaper.html', {'name': name, 'examCode': Code})
        else:
            status = 0
            return HttpResponse(status)


@login_required(login_url='/')
def submitExDetail(request, name):
    if request.method == "POST":
        o = exam_details.objects.filter(examCode=request.POST['examCode'])
        if (o.count() == 0):
            c = request.POST['createdBy']
            if str(request.user) == str(c):
                Code = request.POST['examCode']
                Name = request.POST['examName']
                Time = request.POST['totalTime']
                Mark = 0
                created = request.POST['createdBy']
                detail = exam_details(examCode=Code, examName=Name, totalTime=Time, totalMark=Mark, createdby=created)
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
def finalScore(request, name, code):
    # print(code)
    allQuestion = optionDetail.objects.filter(code=code)
    print(allQuestion.values())
    totalQuest = allQuestion.count()
    corrected = 0
    wrong = 0
    marks = 0
    unAnswer = 0
    if request.method == "POST":
        Nowtime = timezone.now()
        # print(Nowtime.time().hour)
        time = timeManager.objects.get(user=request.user)
        h = abs(Nowtime.time().hour - time.startTime.hour)
        m = abs(Nowtime.time().minute - time.startTime.minute)
        s = abs(Nowtime.time().second - time.startTime.second)
        print(h, m, s)
        duration = h * 60 + m + (s / 60) - 2
        # print("duration")
        print(duration)
        a = exam_details.objects.get(examCode=code)
        # print(a.totalTime)
        if a.totalTime >= duration:
            for i in range(1, totalQuest + 1):
                # print(i)
                try:
                    # print("hello")
                    id = 'q' + str(i)
                    ticked = request.POST[id]
                    qId = int(id[1])
                    quest = optionDetail.objects.get(code=code, q_id=qId)
                    # print(quest.questionMark)
                    if ticked == quest.correctAnswer:
                        corrected = corrected + 1
                        marks = marks + quest.questionMark
                    else:
                        wrong = wrong + 1
                        # print(quest.correctAnswer)
                        # print(qId)
                except:
                    unAnswer += 1
                    pass
            score = scores(user=request.user, score=marks, examCode=code)
            score.save()
            # print(request.POST)
            return render(request, 'submitScore.html',
                          {'name': name, 'user': request.user, 'code': code, 'totalQuest': totalQuest,
                           'correct': corrected, 'wrong': wrong, 'mark': marks, 'Answer': totalQuest - unAnswer})
        else:
            return HttpResponse("You take more than given time, sorry")
