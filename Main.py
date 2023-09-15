import random
from Carte import *
from Joueur import * 
#from colorama import Fore, Back, Style, init

class Main:
	def __init__(self):
		self.couleurs_cartes = ["pique(♠)", "carreau(♦)", "cœur(♥)", "trèfle(♣)"]
		self.pile = [Carte(self.couleurs_cartes[i], j) for i in range(4) for j in range(1, 14)]
		random.shuffle(self.pile)
		self.defausse = [] #là où les joueurs posent leurs cartes
		self.joueurs = [] #liste d'objets contenant les joueurs du jeu
		self.classement = []
		
		r=""
		i = 0

		while len(self.joueurs) < 7 and r.lower() != "s":
			i+=1
			r = input(f"Entrez le nom du joueur {i}, si vous avez suffisament de joueurs tapez 's': ")
			
			if r.lower() == 's' :
				break

			self.joueurs.append(Joueur(r))

		random.shuffle(self.joueurs) #on randomise l'ordre des joueurs
		print("\n")

	def distribuerCartes(self):
		for _ in range(7):
			for i in self.joueurs:
				i.ajoutCarte(self.pile.pop(random.randint(0, len(self.pile) - 1)))

		self.defausse.append(self.pile.pop())

	def phaseDeJeu(self):
		for i in self.joueurs: #les joueurs jouent chacune leur tour
			print(f"\nVoici la carte centrale: {self.defausse[-1].valeur} de {self.defausse[-1].couleur}\n")

			i.voirCartes()#on affiche les cartes du joueur

			r = i.poserCartes(self.defausse[-1]) #le joueur concerné pose sa carte ou en tire une
			
			if r == False : #si il choisi de la tirer
				if self.pile[-1].compatible(self.defausse[-1]) == True: #si le joueur peut joueur la carte tirée
					print(f"La carte tirée est le {self.pile[-1].valeur} de {self.pile[-1].couleur}, elle a donc été jouée")
					self.defausse.append(self.pile.pop())#on l'ajoute à la défausse
				else: #si on ne peut pas la joueur
					print(f"La carte tirée est le {self.pile[-1].valeur} de {self.pile[-1].couleur}, elle a donc été ajoutée à la main de {i.nom}")
					i.ajoutCarte(self.pile.pop())#on l'ajoute à sa main
			
			else : 
				self.defausse.append(r) #on ajoute la carte jouée à la défausse

			i.voirCartes()


	def partieTerminee(self):
		for i in self.joueurs:
			if len(i.main) == 0:#si la main du joueur est vide il a gagné
				return i.nom
		return False

	def classer(self):
		for i in self.joueurs: #on ajoute les scores de chaque joueurs 
			self.classement.append(i.sommePoints())


		for ii in range(len(self.classement) - 1, 1, -1):
			for j in range(ii - 1):
				if self.classement[j + 1][0] > self.classement[j][0]:
					self.classement[j+ 1], self.classement[j] = self.classement[j], self.classement[j + 1] 

		print(self.classement)



main = Main()
main.distribuerCartes()
while main.partieTerminee() == False:
	main.phaseDeJeu()
main.classer()