from django.contrib import admin
from .models import exam_details,questionDetails,optionDetail,scores,timeManager

# Register your models here.
admin.site.register(exam_details)
admin.site.register(questionDetails)
admin.site.register(optionDetail)
admin.site.register(scores)
admin.site.register(timeManager)