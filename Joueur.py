from Carte import *
from colorama import Fore, Back, Style, init

class Joueur:
	def __init__(self, nom):
		couleurs_cartes = [Fore.BLACK + "pique(♠)"+ Style.RESET_ALL, Fore.RED + "carreau(♦)" + Style.RESET_ALL, Fore.RED + "cœur(♥)" + Style.RESET_ALL, Fore.BLACK + "trèfle(♣)" + Style.RESET_ALL]
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
		r = input("Pour choisir votre carte sélectionnez l'indice de la carte que vous voulez jouer ou tirez une carte avec 't': ")

		if r.lower() == 't':
			return False

		r = int(r) - 1

		while self.main[r].compatible(defausse) == False: #tant que le joueur n'a pas joué de carte compatible
			r = input("La carte choisie n'est peut pas être posée, choisissez en une autre ou tirez une carte avec 't': ") #on demande au joueur si il a encore une carte compatible
			
			if r.lower() == 't':#si le joueur préfère tirer une carte
				return False 

			r = int(r) -1 #ne pas avoir d'erreur lorsque j'uilise 'r' comme indice

		e = self.main.pop(r) # on retire la carte utilisée
		
		if e.valeur == 8 :
			for i in range(len(couleurs_cartes) - 1):
				print(i, couleurs_cartes[i], "\n")

			r = int(input("Choisissez la couleur queles autres devront jouer: "))
			e.couleur = couleurs_cartes[r]

		return e # on la retourne également pour la placer dans le défausse

	def sommePoints(self):#somme des points du joueur en fin de partie
		s = 0
		for i in self.main:
			if i.valeur == 8:
				s+=50
			
			if i.valeur == (1 or 2 or 11):
				s+=25

			if i.valeur == (12 or 13):
				s+=10

			else :
				s+= i.valeur

		return(s, self.nom)
