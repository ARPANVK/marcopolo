from django.db import models

# Create your models here.
class QuizQuistions(models.Model):
    question = models.CharField(max_length = 500)
    option_1 = models.CharField(max_length = 100)
    option_2 = models.CharField(max_length = 100)
    option_3 = models.CharField(max_length = 100)
    option_4 = models.CharField(max_length = 100)
    correct_answer = models.CharField(max_length = 100)

def __str__(self):
    return self.question

class UniqCode(models.Model):
    code = models.CharField(max_length= 50)
def __str__(self):
    return self.code

