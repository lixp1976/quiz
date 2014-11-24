from django.contrib.auth.models import User

__author__ = 'djud'

from django.forms.models import ModelForm


class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_active']