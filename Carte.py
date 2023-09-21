from colorama import Fore, Back, Style, init

class Carte:
	def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur
		if self.valeur == 11:
			self.valeur = "Valet"
		if self.valeur == 12:
			self.valeur = "Dame"
		if self.valeur == 13:
			self.valeur = "Roi"

	def compatible(self, carte2):
		if self.valeur == 1 and carte2.valeur == 1:
			return True

		if self.couleur == carte2.couleur or self.valeur == carte2.valeur or ((self.valeur == 8 or carte2.valeur == 8) and (self.valeur != 2 or carte2.valeur !=2)):
			return True

		return False 