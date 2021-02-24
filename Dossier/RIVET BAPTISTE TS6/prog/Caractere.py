from turtle import *
from time import time

NUL = 0 ; FORWARD = 1 ; BACKWARD = 2 ; LEFT = 3 ; RIGHT = 4 ; ROLL = 5 ; SAVE = 6 ; LOAD = 7 
DROITE = 0; GAUCHE = 1; HAUT = 2 ; BAS = 3 

global PLUS
global MOINS 
global BARRE 
global OUVERT 
global FERME 
global Constantes

class Caractere :
	"""Classe contenant un caractere, ainsi que son action associee."""
	
	def __init__(self, caractere, action, option, fonction):
		self.caractere = caractere
		self.action = action
		self.option = option
		self.fonction = fonction
	
	def afficher(self):
		"""Affiche les caracteristiques de l'objet."""
		print("\t", self.caractere, " : ", end='')
		if self.action == 0:
			print("\tRien")
		elif self.action == 1:
			print("\tAvancer")
		elif self.action == 2:
			print("\tReculer")
		elif self.action == 3:
			print("\tTourner a gauche")
		elif self.action == 4:
			print("\tTourner a droite")
		elif self.action == 5:
			print ("\tPivoter à 180 degrés")
		elif self.action == 6:
			print("\tSauvegarder sa position")
		elif self.action == 7:
			print ("\tRestaurer sa position")

class Regle :
	"""Classe contenant une regle : qui indique de transformer un caractere en un autre."""
	def __init__(self, debut, fin):
		self.debut = debut
		self.fin = fin
		
	def afficher(self):
		"""Affiche les caracteristiques de l'objet"""
		print("\t", self.debut.caractere, " ---> ", end='')
		for elemento in self.fin :
			print(elemento.caractere, end='')
		print()
		

class LSysteme :
	"""Classe qui contient le L-Systeme.
	
		Alphabet : Ensemble des caracteres utilises pour le L-Systeme [Caractere*]
		Axiome : Chaine pour n = 0 [Caractere*]
		Regles : Regles appliquees au L-Systeme [Regle*]
		Pas et angle correspondent a ceux utilises lors de la figure [int]
		
		Fonctionnement :
		
		Commencez par initialiser le système.
		Ensuite, generez le avec une valeur n correspondant au niveau du L-systeme
		Enfin, affichez le avec produire
			
		"""
	
	def __init__(self, alphabet, axiome, regles, pas, angle):
		self.alphabet = []
		self.alphabet.extend(alphabet)
		self.axiome = axiome
		self.regles = []
		self.regles.extend(regles)
		self.pas = pas
		self.angle = angle
		self.carChaine = ""
		self.genN = 0
	
	def nouveauCaractere(self, caractere):
		"""Ajoute un nouveau caractere a l'alphabet"""
		self.alphabet.extend(caractere)
		
	def nouvelAxiome(self, axiome):
		"""Remplace l'axiome precedent par un nouveau"""
		self.axiome = axiome
	
	def nouvelleRegle(self, regle):
		"""Ajoute une regles a celles deja indiquees"""
		self.regles.extend(regle)
	
	def nouveauPas(self, pas):
		"""Definit un nouveau pas pour la figure"""
		self.pas = pas
	
	def nouvelAngle(self, angle):
		"""Definit un nouvel angle pour la figure"""
		self.angle = angle
	
	def afficher(self):
		"""Affiche les informations de l'objet"""
		print(self)
		print("Alphabet :")
		for element in self.alphabet :
			element.afficher()
		print("Axiome :\n\t", end='')
		for element in self.axiome :
			print(element.caractere, end='')
		print("\nRegles :")
		for element in self.regles :
			element.afficher()
		print("Pas : ", self.pas, "px")
		print("Angle : ", self.angle, "°\n")
		
	def generer(self, n):
		"""Cree la chaine de caractere du L-systeme a la n-ieme etape"""
		testRegle = False
		chaine = ""
		chaine2 = ""
		for element in self.axiome:
			chaine += str(element.caractere)
		for i in range(n):
			for caractereActuel in chaine:
				for regleAsuivre in self.regles:
					if caractereActuel == regleAsuivre.debut.caractere:
						testRegle = True
						for element in regleAsuivre.fin:
							chaine2 += str(element.caractere)
				if testRegle == False:
					chaine2 += str(caractereActuel)
				testRegle = False
			chaine = str(chaine2)
			chaine2 = ""
		self.carChaine = str(chaine)
		self.genN = n
		
	def produire(self):
		"""Affiche la figure produite par le L-systeme"""
		speed(0)
		hideturtle()
		angleActuel = 0
		pileDeCoordonnees = []
		pileAngles = []
		for carActuel in self.carChaine:
			alphabetConstantes = self.alphabet + Constantes
			for ordreActuel in alphabetConstantes:
				if carActuel == ordreActuel.caractere:
					if ordreActuel.action == 1 and ordreActuel.option != 0 and ordreActuel.fonction == 0:
						forward(ordreActuel.option)
					if ordreActuel.action == 1 and ordreActuel.option == 0 and ordreActuel.fonction == 0:
						forward(self.pas)
					if ordreActuel.action == 1 and ordreActuel.option == 0 and ordreActuel.fonction != 0:
						forward(ordreActuel.fonction.calculer(self.genN))
					
					if ordreActuel.action == 2 and ordreActuel.option != 0 and ordreActuel.fonction == 0:
						backward(ordreActuel.option)
					if ordreActuel.action == 2 and ordreActuel.option == 0 and ordreActuel.fonction == 0:
						backward(self.pas)
					if ordreActuel.action == 2 and ordreActuel.option == 0 and ordreActuel.fonction != 0:
						backward(ordreActuel.fonction.calculer(self.genN))	
						
					if ordreActuel.action == 3 and ordreActuel.option == 0 and ordreActuel.fonction == 0:
						left(self.angle)
						angleActuel += self.angle
					if ordreActuel.action == 3 and ordreActuel.option != 0 and ordreActuel.fonction == 0:
						left(ordreActuel.option)
						angleActuel += ordreActuel.option
					if ordreActuel.action == 3 and ordreActuel.option == 0 and ordreActuel.fonction != 0:
						left(ordreActuel.fonction.calculer(self.genN))
						angleActuel += ordreActuel.fonction.calculer(self.genN)
					
					if ordreActuel.action == 4 and ordreActuel.option == 0 and ordreActuel.fonction == 0:
						right(self.angle)
						angleActuel -= self.angle
					if ordreActuel.action == 4 and ordreActuel.option != 0 and ordreActuel.fonction == 0:
						right(ordreActuel.option)
						angleActuel -= ordreActuel.option
					if ordreActuel.action == 4 and ordreActuel.option == 0 and ordreActuel.fonction != 0:
						right(ordreActuel.fonction.calculer(self.genN))
						angleActuel -= ordreActuel.fonction.calculer(self.genN)					
						
					if ordreActuel.action == 5:
						right(180)
						angleActuel += 180
					if ordreActuel.action == 6:
						pileDeCoordonnees.append(position())
						pileAngles.append(angleActuel)
					if ordreActuel.action == 7:
						allerA = pileDeCoordonnees.pop()
						up()
						goto(allerA[0], allerA[1])
						down()
						nouvelAngle = pileAngles.pop()
						right(angleActuel)
						left(nouvelAngle)
						angleActuel = nouvelAngle
						
	def position(self, position, pixels): #Il faudrait obtenir la taille de l'écran
		"""Definit la position de l'origine de la figure tracee
		
		position : indique l'endroit ou doit etre positionne l'origine
		pixels : indique a quelle distance en pixels l'origine doit etre par rapport a la position indiquee
			
		"""
		speed(0)
		hideturtle()
		up()
		if position == 0:
			forward(759-pixels)
		elif position == 1:
			backward(765-pixels)
		elif position == 2:
			left(90)
			forward(399-pixels)
			right(90)
		elif position == 3:
			left(90)
			backward(391-pixels)
			right(90)
		down()
		
class Fonction:
	"""Définit une fonction"""
	
	def __init__(self, coefficientDirecteur, ordonneeAlOrigine):
		self.coefficientDirecteur = coefficientDirecteur
		self.ordonneeAlOrigine = ordonneeAlOrigine
	
	def calculer(self, n):
		return self.coefficientDirecteur*n+self.ordonneeAlOrigine
						
					
		
PLUS = Caractere("+", LEFT, 0, 0)
MOINS = Caractere("-", RIGHT, 0, 0)
BARRE = Caractere("|", ROLL, 0, 0)
OUVERT = Caractere("[", SAVE, 0, 0)
FERME = Caractere("]", LOAD, 0, 0)

Constantes = [PLUS, MOINS, BARRE, OUVERT, FERME]