from Main import *
from Carte import *

class Joueur:
	def __init__(self):
		self.paquet = []

	def addCarte(self, C):
		self.paquet.append(C)

	def voirCartes(self):
		print(self.paquet)