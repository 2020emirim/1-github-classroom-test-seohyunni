from django.contrib import admin

from .models import Question, Choice


class Questionadmin(admin.ModelAdmin):
    field = ["pub_date", "question_text"]


admin.site.register[Question, Questionadmin]

