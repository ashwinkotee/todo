from django import forms
from django.forms import ModelForm


from .models import *


class TaskTableForm(forms.ModelForm):

    class Meta:
        model = Task_Table
        fields = '__all__'