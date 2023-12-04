# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
import tkinter as tk
from tkinter import messagebox
import random


class MemoryGame(View):
    template_name = 'home/memory_game.html'
    grid_size = 6

    def get(self, request, *args, **kwargs):
        game = self.setup_game()
        return HttpResponse("Game Over")

    def create_new_grid(self):
        self.cartes = list(range(1, (self.grid_size ** 2) // 2 + 1)) * 2
        random.shuffle(self.cartes)
        self.paires_trouvees = 0
        self.plateau = [["X"] * self.grid_size for _ in range(self.grid_size)]
        self.premier_choix = None
        self.verif_en_cours = False

    def create_buttons(self): 
        self.buttons = []
        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                button = tk.Button(self.root, text=" ", width=5, height=2, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i + 1, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, i, j):
        if self.plateau[i][j] == "X" and not self.verif_en_cours:
            value = self.cartes[i * self.grid_size + j]
            self.plateau[i][j] = value
            self.buttons[i][j].config(text=str(value), state=tk.DISABLED)

            if self.premier_choix is None:
                self.premier_choix = (i, j)
            else:
                self.check_match(i, j)

    def check_match(self, i, j):
        choix1 = self.cartes[self.premier_choix[0] * self.grid_size + self.premier_choix[1]]
        choix2 = self.cartes[i * self.grid_size + j]

        if choix1 == choix2:
            self.paires_trouvees += 1
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.premier_choix = None

            if self.paires_trouvees == (self.grid_size ** 2) // 2:
                self.create_new_grid()
                self.update_score_label()
                self.refresh_buttons()
        else:
            self.verif_en_cours = True
            self.root.after(1000, lambda: self.hide_cards(self.premier_choix, (i, j)))

    def hide_cards(self, index1, index2):
        self.plateau[index1[0]][index1[1]] = "X"
        self.plateau[index2[0]][index2[1]] = "X"

        for i, j in [index1, index2]:
            self.buttons[i][j].config(text=" ", state=tk.NORMAL)

        self.premier_choix = None
        self.verif_en_cours = False

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}")

    def refresh_buttons(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)

    def setup_game(self):
        self.root = tk.Tk()
        self.score = 0
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 16))
        self.score_label.grid(row=0, column=0, columnspan=self.grid_size)
        self.create_new_grid()
        self.create_buttons()
        self.root.mainloop()

def index(request):
    return render(request, 'home/index.html')
def game_page(request):
    return render(request, 'home/memory_game.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import Formulaire

def inscription(request):
    if request.method == 'POST':
        formulaire = Formulaire(request.POST)
        if formulaire.is_valid():
            utilisateur = formulaire.save()
            login(request, utilisateur)
            return redirect('accueil')  # Redirigez vers la page d'accueil ou toute autre page après l'inscription réussie
    else:
        formulaire = Formulaire()
    return render(request, 'registration/inscription.html', {'formulaire': formulaire})