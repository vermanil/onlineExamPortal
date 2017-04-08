from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class exam_details(models.Model):
    examCode = models.TextField()
    examName = models.TextField()
    totalTime = models.TimeField()
    totalMark = models.IntegerField()
    createdby = models.TextField()

class questionDetails(models.Model):
    code = models.TextField()
    question_id = models.IntegerField()
    correctAnswer = models.TextField()

class optionDetail(models.Model):
    q_id = models.IntegerField()
    question = models.TextField(default="sdfg")
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()

class scores(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()
    examCode = models.ForeignKey(exam_details)
    rank = models.IntegerField()