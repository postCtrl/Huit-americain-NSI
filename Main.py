import random
from Carte import *
from Joueur import * 
from colorama import Fore, Back, Style, init

regles = "https://jeuxetlogique.fr/wp-content/uploads/2021/12/Le-8-americain_txt.pdf\n"

class Main:
	def __init__(self):
		couleurs_cartes = [Fore.BLACK + "pique(♠)"+ Style.RESET_ALL, Fore.RED + "carreau(♦)" + Style.RESET_ALL, Fore.RED + "cœur(♥)" + Style.RESET_ALL, Fore.BLACK + "trèfle(♣)" + Style.RESET_ALL]
		self.pile = [Carte(couleurs_cartes[i], j) for i in range(4) for j in range(1, 14)]
		random.shuffle(self.pile)
		self.defausse = [] #là où les joueurs posent leurs cartes
		self.joueurs = [] #liste d'objets contenant les joueurs du jeu
		self.classement = []
		self.tours = 0
		print(regles)#ligne codée par yanis ouachtati 
		
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
		while True:
			for i in self.joueurs: #les joueurs jouent chacune leur tour
				print(f"\nVoici la carte centrale: {self.defausse[-1].valeur} de {self.defausse[-1].couleur}\n")

				i.voirCartes()#on affiche les cartes du joueur
				
				if self.defausse[-1].valeur == 2  and self.tours > 0:
					for _ in range(2):
						i.ajoutCarte(self.pile.pop())
					print(f"\nLe tour de {i.nom} a été passé")
					continue 

				rep = i.poserCartes(self.defausse[-1]) #le joueur concerné pose sa carte ou en tire une

				if rep == False : #si il choisi de la tirer
					if self.pile[-1].compatible(self.defausse[-1]) == True: #si le joueur peut joueur la carte tirée
						print(f"La carte tirée est le {self.pile[-1].valeur} de {self.pile[-1].couleur}, elle a donc été jouée")
						self.defausse.append(self.pile.pop())#on l'ajoute à la défausse
						rep = True
						continue
					else: #si on ne peut pas la joueur
						print(f"La carte tirée est le {self.pile[-1].valeur} de {self.pile[-1].couleur}, elle a donc été ajoutée à la main de {i.nom}")
						i.ajoutCarte(self.pile.pop())#on l'ajoute à sa main
						continue
				try:
					if rep.lower() != 'carte':
						for _ in range(2):
							i.ajoutCarte(self.pile.pop())

				except AttributeError:
					if rep.valeur == "Valet" and len(self.joueurs) > 2:
						self.joueurs.reverse()
						print("L'ordre de jeu a été inversé\n")
					self.defausse.append(rep) #on ajoute la carte jouée à la défausse

				continue

				if len(i.main) == 0:
					return True
			self.tours += 1

	def classer(self):
		for i in self.joueurs: #on ajoute les scores de chaque joueurs 
			self.classement.append(i.sommePoints())


		for ii in range(len(self.classement) - 1, 1, -1):
			for j in range(ii - 1):
				if self.classement[j + 1][0] > self.classement[j][0]:
					self.classement[j+ 1], self.classement[j] = self.classement[j], self.classement[j + 1] 

		print(f"{self.classement[0][1]} a gagné en {self.tours} tours! Félicitations !\n")

		for iii in range(1, len(self.classement)):
			print(f"{self.classement[iii][1]} est arrivé {iii}ème avec {self.classement[iii][0]} points")


main = Main()
main.distribuerCartes()
main.phaseDeJeu()
main.classer()