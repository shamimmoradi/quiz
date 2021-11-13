from django.db import models
from django.db.models.deletion import CASCADE
from  django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length= 200)

    def __str__(self):
        return self.title

    
class QuizQuestion(models.Model):
    title = models.TextField(max_length=100)
    ctegory = models.ForeignKey(Category , on_delete= models.CASCADE )
    question = models.CharField(max_length = 500)
    a1 = models.CharField(max_length=200)
    a2 = models.CharField(max_length=200)
    a3 = models.CharField(max_length=200)
    a4 = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    
class Quiz(models.Model):
    title = models.TextField(max_length=100)
    questions =  models.ForeignKey(QuizQuestion , on_delete= models.CASCADE )
    time = models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return self.title 
    
    