from Carte import *
#from colorama import Fore, Back, Style, init

class Joueur:
	def __init__(self, nom):
		self.main = []
		self.nom = nom

	def ajoutCarte(self, C):
		self.main.append(C)
		print(f"La carte {C.valeur} de {C.couleur} a été distribuée à {self.nom}")

	def voirCartes(self):
		index = 0
		for i in self.main:
			index += 1
			print(f"{index}. {self.nom} a le {i.valeur} de {i.couleur}")
		print("")

	def poserCartes(self, defausse):
		r = int(input("Pour choisir votre carte sélectionnez l'indice de la carte que vous voulez jouer: ")) - 1

		while self.main[r].compatible(defausse) == False: #tant que le joueur n'a pas joué de carte compatible
			r = input("La carte choisie n'est peut pas être posée, choisissez en une autre ou tirez une carte avec 't': ") #on demande au joueur si il a encore une carte compatible
			
			if r.lower() == 't':#si le joueur préfère tirer une carte
				return False 

			r = int(r) #ne pas avoir d'erreur lorsque j'uilise 'r' comme indice

		e = self.main.pop(r) # on retire la carte utilisée	
		return e # on la retourne également pour la placer dans le défausse
