from django.db import models

# Create your models here.

class exam_details(models.Model):
    examCode = models.TextField()
    examName = models.TextField()
    totalTime = models.IntegerField()
    totalMark = models.IntegerField()
    createdby = models.TextField()

class questionDetails(models.Model):
    code = models.ForeignKey(exam_details.examCode)
    question_id = models.IntegerField()
    correctAnswer = models.TextField()

class optionDetails(models.Model):
    id = models.ForeignKey(questionDetails.question_id)
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()