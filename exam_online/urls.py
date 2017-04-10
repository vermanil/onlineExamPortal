from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/(?P<name>[\S]+)/login/?$', views.candidateLogin, name="candidateLogin"),
    url(r'^accounts/(?P<name>[\S]+)/register/?$', views.candidateRegister, name="candidateRegister"),
    url(r'^(?P<name>[\S]+)/exam/?$', views.exam, name="exam"),
    url(r'^accounts/(?P<name>[\S]+)/logout/?$', views.Clogout, name="logout"),
    url(r'^(?P<name>[\S]+)/exam/examdetails/?$', views.aboutExam, name="aboutExam"),
    url(r'^(?P<name>[\S]+)/exam/editSet/?$', views.setEditQues, name="setEditQues"),
    url(r'^(?P<name>[\S]+)/exam/setQues/?$', views.setQues, name="setQues"),
    url(r'^(?P<name>[\S]+)/exam/start/?$', views.startExam, name="startExam"),
    url(r'^(?P<name>[\S]+)/exam/session/?$', views.sessionStart, name="sessionStart"),
    url(r'^(?P<name>[\S]+)/exam/selectCode/?$', views.selectExamCode, name="selectExamCode"),
    url(r'^(?P<name>[\S]+)/exam/board/?$', views.seeLeaderboard, name="seeLeaderboard"),
    url(r'^(?P<name>[\S]+)/exam/(?P<code>[\S]+)/edit/?$', views.editQuestionForm, name="editQuestionForm"),
    url(r'^(?P<name>[\S]+)/exam/scores/?$', views.CandidateScore, name="CandidateScore"),
    url(r'^(?P<name>[\S]+)/exam/allListBoard/?$', views.showListBoard, name="showListBoard"),
    url(r'^(?P<name>[\S]+)/exam/submitQues/?$', views.submitQuestion, name="submitQuestion"),
    url(r'^(?P<name>[\S]+)/exam/submitExDetails/?$', views.submitExDetail, name="submitExDetail"),
    url(r'^(?P<name>[\S]+)/exam/session/(?P<code>[\S]+)/done?$', views.finalScore, name="finalScore"),
    url(r'^(?P<name>[\S]+)/exam/updateQues?$', views.updateQues, name="updateQues"),
    url(r'^(?P<name>[\S]+)/exam/time?$', views.timeManage, name="timeManage"),
]