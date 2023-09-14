import random
from Carte import *
from Joueur import * 

class Main:
	def __init__(self):
		self.couleurs_cartes = ["pique", "carreau", "cœur", "trèfle"]
		self.pile = [Carte(self.couleurs_cartes[i], j) for i in range(4) for j in range(1, 14)]
		self.defausse = [] #là où les joueurs posent leurs cartes
		self.joueurs = [] #liste d'objets contenant les joueurs du jeu
		r=""
		i = 0
		while len(self.joueurs) < 1 and r.lower() != "s":
			i+=1
			r = input(f"Entrez le nom du joueur {i}, si vous avez suffisament de joueurs tapez 's': ")
			self.joueurs.append(Joueur(r))

	def distribuerCartes(self, joueurs):
		for i in self.joueurs:
			i.addCarte(self.pile.pop(random.int(len(self.pile))))


main = Main()
