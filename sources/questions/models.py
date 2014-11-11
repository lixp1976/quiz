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


class QuestionType(models.Model):
    name = models.CharField(max_length=128)


class Question(models.Model):
    html_text = models.TextField()
    image = models.ImageField()
    question_set = models.ForeignKey(QuestionSet, null=False, blank=False)
    question_type = models.ForeignKey(QuestionType)


class Answer(models.Model):
    html_text = models.TextField()
    image = models.ImageField()
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question)