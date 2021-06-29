import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Setting the default model manager
    objects = models.Manager()

    question_text = models.CharField(max_length=200)
    id = models.IntegerField(default=1, primary_key=True)
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    # Setting the default model manager
    objects = models.Manager()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
