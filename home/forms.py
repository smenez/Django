from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person

class Formulaire(UserCreationForm) :
    email = forms.EmailField()

    class Meta():
        model = Person
        fields = ['first_name', 'last_name', 'email_address', "password"]