from django.contrib import admin
from .models import Person
from .models import Message

admin.site.register(Person)
admin.site.register(Message)
