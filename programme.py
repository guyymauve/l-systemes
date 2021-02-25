from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from time import *
from os import system

global fichierActuel
fichierActuel = ""

#///////////////////FONCTIONS BARRE D'OUTILS////////////////

def new():
	"""
		Crée un nouveau fichier texte. Sauvegarde d'abord le fichier ouvert.
	"""
	global fichierActuel
	if fichierActuel == "":
		if askyesno("Fichier non sauvegardé", "Voulez-vous sauvegarder le fichier actuel ?"):
			enregistrerSous()
			realNew()
		else:
			realNew()
	else:
		fichier = open(fichierActuel, "r")
		contenu = fichier.read()
		mot = str(entree.get("0.0", "end"))
		if contenu == mot:
			fichier.close()
			realNew()
		else:
			fichier.close()
			if askyesno("Fichier non sauvegardé", "Voulez-vous sauvegarder le fichier actuel ?"):
				enregistrer()
				realNew()
			else:
				realNew()
				
def realNew():
	"""
		Appelée par new() pour effacer le texte à l'écran
	"""
	global fichierActuel
	entree.delete("0.0", "end")
	fichierActuel = ""
	
def undo():
	"""
		Annule la dernière action.
	"""
	entree.edit_undo()
	
def redo():
	"""
		Annule les actions annulées.
	"""
	entree.edit_redo()

def enregistrer():
	"""
		Enregistre le code dans un fichier.
	"""
	global fichierActuel
	mot = str(entree.get("0.0", "end"))
	if fichierActuel == "":
		enregistrerSous()
	elif fichierActuel == ".txt":
		return 1
	else:
		fichier = open(fichierActuel, "w")
		fichier.write(mot)
		fichier.write("\n")
		fichier.close()
		
def enregistrerSous():
	"""
		Enregistre le code sous dans un fichier.
	"""
	global fichierActuel
	fichierActuel = str(asksaveasfilename(title="Enregistrer sous", filetypes=[("txt files", ".txt"),("all files", ".*")]))
	txtFind = fichierActuel.find(".txt")
	if txtFind == -1:
		fichierActuel += ".txt"
	enregistrer()

def ouvrir():
	"""
		Ouvre un fichier et l'affiche.
	"""
	global fichierActuel
	filepath = askopenfilename(title="Ouvrir un fichier", filetypes=[("txt files", ".txt"),("all files", ".*")])
	if filepath == "":
		return 1
	fichier = open(filepath, "r")
	contenu = fichier.read()
	fichier.close()
	entree.delete("0.0", "end")
	entree.insert("insert", contenu)
	fichierActuel = str(filepath)

def buildAndRun():
	build()
	sleep(1)
	run()
	
def build():
	fichier2 = open("nomFichier.py", "w")
	fichier2.write('def nomFichier():\n\treturn "')
	fichier2.write(fichierActuel)
	fichier2.write('"')
	fichier2.close()
	system("batch.bat")
	
def run():
	enregistrer()
	system("batch2.bat")
	
def addLSysteme():
	entree.insert("insert", "LSysteme()\n{\n\tAlphabet = []\n\tAxiome = \n\tRegles = []\n\tPas = \n\tAngle = \n}")

def addCaractere():
	entree.insert("insert", "Caractere( = ())")

def addGenerer():
	entree.insert("insert", "Generer()\n{\n\tN = \n}")
	
def addRegle():
	entree.insert("insert", "Regle( = ->)")

#///////////////////INTERFACE//////////////////
	
fenetre = Tk() #Fenetre principale (la fenetre Windows)

#----Def Icones Barre D'Outils----
photoRun = PhotoImage(file="./gif/run.gif") #Executer
photoBuild = PhotoImage(file="./gif/build.gif") #Compiler
photoBuildAndRun = PhotoImage(file="./gif/buildAndRun.gif") #Compiler et Executer
photoFileNew = PhotoImage(file="./gif/filenew.gif") #Nouveau
photoFileOpen = PhotoImage(file="./gif/fileopen.gif") #Ouvrir
photoFileSave = PhotoImage(file="./gif/filesave.gif") #Enregistrer
photoFileSaveAll = PhotoImage(file="./gif/filesaveall.gif") #Enregistrer Sous
photoUndo = PhotoImage(file="./gif/undo.gif") #Annuler (Ctrl+Z)
photoRedo = PhotoImage(file="./gif/redo.gif") #Revenir (Ctrl+Y)
#---------------------------------


#----Barre D'Outils
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau", command=new)
menu1.add_command(label="Ouvrir", command=ouvrir)
menu1.add_command(label="Enregistrer", command=enregistrer)
menu1.add_command(label="Enregistrer sous", command=enregistrerSous)
menu1.add_command(label="Imprimer")
menu1.add_command(label="Quitter")

menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Annuler", command=undo)
menu2.add_command(label="Rétablir", command=redo)
menubar.add_cascade(label="Édition", menu=menu2)

fenetre.config(menu=menubar)


P0 = PanedWindow(fenetre, orient=VERTICAL, height=720, width=1280)
P0.pack(side=LEFT, expand=Y, fill=BOTH)

P1 = PanedWindow(P0, orient=HORIZONTAL)
P2 = PanedWindow(P1, orient=VERTICAL)

entree = ScrolledText(P2, height=33)

#----

P2.add(entree)
P2.add(Label(P2, text="Log", background="blue", anchor="center"))

P11 = PanedWindow(P1, orient=VERTICAL)

P11.add(Button(P11, text="LSysteme()", width=20, command=addLSysteme))
P11.add(Button(P11, text="Generer()", width=20, command=addGenerer))
P11.add(Button(P11, text="Caractere()", width=20, command=addCaractere))
P11.add(Button(P11, text="Regle()", width=20, command=addRegle))
P11.add(Frame(P11))

P1.add(P11)
P1.add(P2)

P01 = PanedWindow(fenetre, orient=HORIZONTAL)
P011 = PanedWindow(fenetre, orient=HORIZONTAL, borderwidth=2, relief=RIDGE)
P012 = PanedWindow(fenetre, orient=HORIZONTAL, borderwidth=2, relief=RIDGE)
P013 = PanedWindow(fenetre, orient=HORIZONTAL, borderwidth=2, relief=RIDGE)

P011.add(Button(P011, image=photoFileNew, command=new))
P011.add(Button(P011, image=photoFileOpen, command=ouvrir))
P011.add(Button(P011, image=photoFileSave, command=enregistrer))
P011.add(Button(P011, image=photoFileSaveAll, command=enregistrerSous))

P01.add(P011)

P012.add(Button(P012, image=photoUndo, command=undo))
P012.add(Button(P012, image=photoRedo, command=redo))

P01.add(P012)

P013.add(Button(P013, image=photoBuild, command=build))
P013.add(Button(P013, image=photoRun, command=run))
P013.add(Button(P013, image=photoBuildAndRun, command=buildAndRun))

P01.add(P013)

P01.add(Frame(P01))

P0.add(P01)
P0.add(P1)

P0.add(P1)
P0.pack()


fenetre.mainloop()