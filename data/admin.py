from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):
    list_display =['id', 'title',]

class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_right',]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields= ['title', 'quiz']
    list_display = ['title', 'quiz',]

    inlines = [AnswerInline,]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']
