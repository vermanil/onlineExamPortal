from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class exam_details(models.Model):
    examCode = models.TextField()
    examName = models.TextField()
    totalTime = models.IntegerField()
    totalMark = models.IntegerField()
    createdby = models.ForeignKey(User)

class questionDetails(models.Model):
    code = models.ForeignKey(exam_details)
    question_id = models.IntegerField()
    correctAnswer = models.TextField()

class optionDetail(models.Model):
    q_id = models.ForeignKey(questionDetails)
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()

class scores(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()
    examCode = models.ForeignKey(exam_details)
    rank = models.IntegerField()