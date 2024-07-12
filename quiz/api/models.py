from django.db import models

# Create your models here.
class Quiz(models.Model):
  name = models.CharField(max_length=100)
  time_limit = models.IntegerField() # in minutes
  no_of_questions = models.IntegerField(default=0)
  
class Question(models.Model):
  quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
  text = models.CharField(max_length=255)

class Option(models.Model):
  question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
  text = models.CharField(max_length=255)
  is_correct = models.BooleanField(default=False)