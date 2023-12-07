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
from .forms import CreerUtilisateur
from . import models
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    return render(request, 'home/index.html')
def classement(request):
    return render(request, 'home/classement.html')
def game_page(request):
    return render(request, 'home/gamemode.html')
# @login_required(login_url='gamemode.html')
def memorygame(request):
    return render(request, 'home/memory_game.html')
# @login_required(login_url='gamemode.html')
def mortsubite(request):
    return render(request, 'home/mortsubite.html')
def profil(request):
    return render(request, 'home/profil.html')




def Inscription(request) :
    form = CreerUtilisateur()
    if request.method == "POST" :
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('connexion.html')
    else:
        form = CreerUtilisateur()
        print('Pb connexion')
        if 'submitted' in request.GET:
            submitted = True
    context={'form':form}
    return render(request, "home\\inscription.html", {'form': form})



def Connexion(request) :
    submitted = False
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('index.html')
        else:
            messages.info(request, "Utilisateur et/ou Mot de passe incorrect")
    return render(request, 'home/connexion.html')

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('home/connexion.html')