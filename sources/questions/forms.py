from django.forms.models import modelformset_factory
from questions.models import QuestionSet

__author__ = 'djud'

from django import forms


class QuestionSetForm(forms.ModelForm):

    class Meta():
        model = QuestionSet
        fields = ['title', 'max_time', 'max_answers', 'description']

    title = forms.CharField(label='Название')
    max_time = forms.IntegerField(label='Время, отведенное на тест')
    max_answers = forms.IntegerField(label='Сколько вариантов ответов '
                                           'отображать')
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      {'cols': '50', 'rows': '4'}
                                  ))


QuestionSetFormSet = modelformset_factory(QuestionSet, QuestionSetForm, extra=0)