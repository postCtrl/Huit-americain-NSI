class Carte:
	def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur

	def compatible(self, carte2):
		
		if self.couleur == carte2.couleur and self.valeur == carte2.valeur:
			return True

		return False 