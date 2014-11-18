from django.forms.models import modelformset_factory
from questions.models import QuestionSet, Question, Answer

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


class QuestionForm(forms.ModelForm):

    class Meta():
        model = Question
        fields = ['html_text', 'image']

    html_text = forms.CharField(label='Текст вопроса',
                                widget=forms.Textarea(
                                    {'cols': '50', 'rows': '4'}
                                ))
    image = forms.ImageField(required=False)

QuestionFormSet = modelformset_factory(Question, QuestionForm, extra=0)


class AnswerForm(forms.ModelForm):

    class Meta():
        model = Answer
        fields = ['html_text', 'image', 'is_right']

    html_text = forms.CharField(label='Текст ответа',
                                widget=forms.Textarea(
                                    {'cols': '50', 'rows': '4'}
                                ))
    image = forms.ImageField(label='Картинка', required=False)
    is_right = forms.BooleanField(label='Это правильный вариант',
                                  required=False)


AnswerFormSet = modelformset_factory(Answer, AnswerForm, extra=0)