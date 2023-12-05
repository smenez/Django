from . import models
from django import forms
from django.forms import ModelForm
from .models import Formulaire

class FormulaireForm(ModelForm) :
    class Meta :
        model = Formulaire
        fields = ('pseudo', 'email', 'password',)