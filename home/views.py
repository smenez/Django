from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def jeu(request):
    return render(request, 'home/jeu.html')