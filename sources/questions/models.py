__author__ = 'djud'

from django.db import models


class QuestionSet(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    max_time = models.IntegerField(default=0,
                                   help_text='Максимальное время на прохождение (в секундах)')
    max_answers = models.IntegerField(default=0,
                                      help_text='Максимальное кол-во вариантов ответов')


class Mark(models.Model):
    mark = models.IntegerField()
    image = models.ImageField()
    text = models.CharField(max_length=1024)


class MarkSettings(models.Model):
    mark = models.ForeignKey(Mark)
    min_answers = models.IntegerField()
    question_set = models.ForeignKey(QuestionSet)


class Question(models.Model):
    html_text = models.TextField(default='')
    image = models.ImageField(default=None, null=True)
    question_set = models.ForeignKey(QuestionSet, null=False, blank=False)
    updated = models.DateTimeField(null=True, blank=False, default=None)


class Answer(models.Model):
    html_text = models.TextField(default='')
    image = models.ImageField(default=None, null=True)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, null=False, blank=False)
    updated = models.DateTimeField(null=True, blank=False, default=None)