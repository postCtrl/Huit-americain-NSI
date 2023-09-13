from Carte import *
from Joueur import * 

class Main:
	def __init__(self, joueurs):
		self.couleurs_cartes = ["pique", "carreau", "cœur", "trèfle"]
		self.pile = [for i in range(4) for j in range(13) Carte(couleurs_cartes[i], j) ] # pile du jeu
		self.defausse = [] #là où les joueurs posent leurs cartes
		self.joueurs = joueurs #liste d'objets contenant les joueurs du jeu

	def distribuerCartes(self, Joueurs):

