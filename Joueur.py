from Carte import *

class Joueur:
	def __init__(self, nom):
		self.paquet = []
		self.nom = nom

	def ajoutCarte(self, C):
		self.paquet.append(C)

	def voirCartes(self):
		index = 0
		for i in self.paquet:
			index += 1
			print(f"{index}. {self.nom} a le {i.valeur} de {i.couleur}")

	def poserCartes(self, defausse):
		r = int(input("Pour choisir votre carte sélectionnez l'indice de la carte que vous voulez jouer: ")) - 1

		if self.paquet[r].couleur == defausse.couleur or self.paquet[r] == defausse.valeur:
			return self.paquet[r]

		return False


