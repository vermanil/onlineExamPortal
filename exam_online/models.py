from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class exam_details(models.Model):
    examCode = models.TextField()
    examName = models.TextField()
    totalTime = models.IntegerField()
    totalMark = models.IntegerField()
    createdby = models.TextField()


class questionDetails(models.Model):
    code = models.TextField()
    question_id = models.IntegerField()


class optionDetail(models.Model):
    code = models.TextField()
    q_id = models.IntegerField()
    question = models.TextField()
    questionMark = models.IntegerField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correctAnswer = models.TextField()


class scores(models.Model):
    user = models.TextField()
    score = models.IntegerField()
    examCode = models.TextField()


class timeManager(models.Model):
    user = models.TextField()
    startTime = models.TimeField(default=timezone.now())
