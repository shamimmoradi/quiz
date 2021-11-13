from django.contrib import admin
from quizapp import  *
from quizapp.models import Category, Quiz, QuizQuestion
# Register your models here.

admin.site.register(Category)
admin.site.register(QuizQuestion)
admin.site.register(Quiz)