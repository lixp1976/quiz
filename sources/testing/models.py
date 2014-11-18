from django.contrib.auth.models import User
from questions.models import QuestionSet, Answer, Question

__author__ = 'djud'

from django.db import models


class TestingQuestion(models.Model):
    question = models.ForeignKey(Question)
    index = models.IntegerField()
    answered = models.BooleanField(default=False)
    next = models.ForeignKey('self', null=True, related_name='qnext')
    previous = models.ForeignKey('self', null=True, related_name='qprev')
    testing = models.ForeignKey('testing.Testing')
    # TODO: нужно ли позволять переотвечать на вопросы?

    @property
    def is_last(self):
        return self.next is None


class Testing(models.Model):
    user = models.ForeignKey(User)
    question_set = models.ForeignKey(QuestionSet)
    started = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, default=None)
    deadline = models.DateTimeField()
    current_question = models.ForeignKey(TestingQuestion, null=True,
                                         related_name='cur_testing')

    def next_question(self):
        if self.current_question.next:
            self.current_question = self.current_question.next
            if self.current_question.answered:
                return self.next_question()
        else:
            questions = list(
                self.testingquestion_set.all().filter(answered=False))
            if len(questions) > 0:
                self.current_question = questions[0]
            else:
                self.current_question = None

    @property
    def unanswered_questions(self):
        return list(self.testingquestion_set.all().filter(
            testing=self, answered=False).order_by('index'))


class TestingLog(models.Model):
    testing = models.ForeignKey(Testing)
    datetime = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)