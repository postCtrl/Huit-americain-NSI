from Carte import *

class Joueur:
	def __init__(self, nom):
		self.paquet = []
		self.nom = nom

	def addCarte(self, C):
		self.paquet.append(C)

	def voirCartes(self):
		print(self.paquet)



