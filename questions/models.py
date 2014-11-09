__author__ = 'djud'

from django.db import models


class Mark(models.Model):
    mark = models.IntegerField()
    image = models.ImageField()
    text = models.CharField(max_length=1024)


class QuestionSet(models.Model):
    title = models.CharField(max_length=256)
    max_time = models.IntegerField(default=0,
                                   help_text='Максимальное время на прохождение')


class MarkSettings(models.Model):
    mark = models.ForeignKey(Mark)
    min_answers = models.IntegerField()
    question_set = models.ForeignKey(QuestionSet)


class QuestionType(models.Model):
    pass


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