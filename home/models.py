from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(default='salut@gmail.com')
    password = models.CharField(max_length=30, default=123)

    def __str__(self) :
        return self.first_name, self.last_name, self.email_address, self.password
    
class Message(models.Model):
    titre = models.TextField(max_length=2)
    contenu = models.TextField(max_length=50)
    date = models.DateField()
