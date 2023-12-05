from django.db import models

class Formulaire(models.Model) :
    pseudo = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)