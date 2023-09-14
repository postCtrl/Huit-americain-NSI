import random
from Carte import *
from Joueur import * 

class Main:
	def __init__(self):
		self.couleurs_cartes = ["pique(♠)", "carreau(♦)", "cœur(♥)", "trèfle(♣)"]
		self.pile = [Carte(self.couleurs_cartes[i], j) for i in range(4) for j in range(1, 14)]
		self.defausse = [] #là où les joueurs posent leurs cartes
		self.joueurs = [] #liste d'objets contenant les joueurs du jeu
		
		r=""
		i = 0

		while len(self.joueurs) < 7 and r.lower() != "s":
			i+=1
			r = input(f"Entrez le nom du joueur {i}, si vous avez suffisament de joueurs tapez 's': ")
			
			if r.lower() == 's' :
				break

			self.joueurs.append(Joueur(r))

		print("\n")

	def distribuerCartes(self):
		for _ in range(7):
			for i in self.joueurs:
				i.ajoutCarte(self.pile.pop(random.randint(0, len(self.pile) - 1)))

		self.defausse.append(self.pile.pop())

	def phaseDeJeu(self):
		print(f"Voici la carte centrale: {self.defausse[-1].valeur} de {self.defausse[-1].couleur}\n")

		for i in self.joueurs: #les joueurs jouent chacune leur tour
			i.voirCartes()#on affiche les cartes du joueur

			r = i.poserCartes(self.defausse[-1]) #le joueur concerné pose sa carte ou en tire une
			
			if r == False : #si il choisi de la tirer
				if self.pile[-1].compatible(self.defausse[-1]) == True: #si le joueur peut joueur la carte tirée
					self.defausse.append(self.pile.pop())#on l'ajoute à la défausse
				else: #si on ne peut pas la joueur
					i.ajoutCarte(self.pile.pop())#on l'ajoute à sa main
			
			else : 
				self.defausse.append(r) #on ajoute la carte jouée à la défausse


main = Main()
main.distribuerCartes()
main.phaseDeJeu()