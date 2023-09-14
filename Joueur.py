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
		print("")

	def poserCartes(self, defausse):
		r = input("Pour choisir votre carte sélectionnez l'indice de la carte que vous voulez jouer: ") - 1

		while self.paquet[r].couleur != defausse.couleur or self.paquet[r] != defausse.valeur:
			r = input("La carte choisie n'est peut pas être posée, choisissez en une autre ou tirez une carte avec 't': ")
			
			if r.lower() == 't':
				return False 

			r = int(r) 

		return self.paquet[r]