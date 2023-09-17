class Carte:
	def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur

	def compatible(self, carte2):
		
		if self.couleur == carte2.couleur or self.valeur == carte2.valeur or self.valeur == 8:
			return True

		return False 