# myapp/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.template import loader
import tkinter as tk
from tkinter import messagebox
import random
from .forms import FormulaireForm
from . import models
from django import forms


def index(request):
    return render(request, 'home/index.html')
def classement(request):
    return render(request, 'home/classement.html')
def game_page(request):
    return render(request, 'home/gamemode.html')
def memorygame(request):
    return render(request, 'home/memory_game.html')
def mortsubite(request):
    return render(request, 'home/mortsubite.html')




def inscription(request) :
    submitted = False
    if request.method == "POST" :
        form = FormulaireForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormulaireForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "home\\form.html", {'form': form})