from django.forms import *
from .models import *
from django import forms
from django.db.models import Q
from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'
