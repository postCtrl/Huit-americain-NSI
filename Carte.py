from colorama import Fore, Back, Style, init

class Carte:
	def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur

	def compatible(self, carte2):
		
		if self.valeur == 1 and carte2.valeur == 1:
			return True

		if self.couleur == carte2.couleur or self.valeur == carte2.valeur or self.valeur == 8:
			return True

		return False 