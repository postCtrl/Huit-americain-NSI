from Carte import *

class Joueur:
	def __init__(self, nom):
		self.paquet = []
		self.nom = nom

	def addCarte(self, C):
		self.paquet.append(C)

	def voirCartes(self):
		for (i, index )in enumerate(self.paquet, start=1):
			print(f"{index + 1} {self.nom} a le {i.valeur} de {i.couleur}")

	def poserCartes(self, defausse):
		print("Pour choisir votre carte sélectionnez l'indice de la carte que vous voulez jouer: ")


