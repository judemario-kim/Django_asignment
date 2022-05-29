import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    score = models.IntegerField(default=100)
    num_of_question = models.IntegerField(default=0)
    def __str__(self):
        return self.exam_name

class Question(models.Model): #문제
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    content = models.TextField()#문제내용
    # 원하는것: admin에서 문제 생성시 선택지를
    # 3/5/7/9/11과 같이 만들면 문자열 스플릿기능을 통해
    # 각각 나누고 자동으로 Choice생성
    pub_date = models.DateField('date published', default=timezone.now)
    correct = models.IntegerField(default=0)
    correct_rate = models.FloatField(default=100.0)
    
    def __str__(self):
        return self.question_text
    
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text