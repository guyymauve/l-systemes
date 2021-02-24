from nomFichier import *

mon_fichier = open(nomFichier(), "r")
compiler = open("compile.py", "w")
contenu = mon_fichier.read()
strbuff = ""
removeBuff = ""
boolL = False
boolGenerer = False
compteurPos = 0

compiler.write("from Caractere import *\n\n")

while contenu != "":
	boolN = False
	for element in contenu:
		if element == '\n':
			boolN = True
		if boolN == False:	
			strbuff += element
	# print(strbuff)
	removeBuff = str(strbuff) + '\n'
	
	a1 = strbuff.find("Caractere")
	a2 = strbuff.find("Regle")
	a3 = strbuff.find("LSysteme")
	a4 = strbuff.find("Generer")
	a5 = strbuff.find("Fonction")
	
	autre = strbuff.find("nouveauCaractere")
	if autre != -1:
		a1 = -1
	autre = strbuff.find("nouvelleRegle")
	if autre != -1:
		a2 = -1
	
	
	strbuff = strbuff.replace("\t", "")
	
	if boolL == True and a2 != -1:
		a2 = -1
	
	if a1 != -1:
		strbuff = strbuff.replace("Caractere(", "")
		chara = ""
		chara = strbuff[0]
		strbuff = strbuff.replace(chara, "", 1)
		strbuff = strbuff.replace(" ", "")
		strbuff = strbuff.replace("=", "")
		strbuff = strbuff.replace("))", "")
		action = ""
		boolPar = False
		for element in strbuff:
			if element == '(':
				boolPar = True
			if boolPar == False:
				action += element
		strbuff = strbuff.replace(action, "")
		fctvar = ""
		fctvar = strbuff.replace("(", "")
		option = ""
		fonction = ""
		if fctvar.isdigit():
			option = str(fctvar)
			fonction = "0"
		else :
			option = "0"
			fonction = str(fctvar)
		
		compiler.write(chara)
		compiler.write(' = Caractere("')
		compiler.write(chara)
		compiler.write('", ')
		compiler.write(action)
		compiler.write(", ")
		compiler.write(option)
		compiler.write(", ")
		compiler.write(fonction)
		compiler.write(")")
		compiler.write("\n")
		
	elif a2 != -1:
		strbuff = strbuff.replace("Regle(", "")
		nomVariable = ""
		boolPar = False
		for element in strbuff:
			if element == " " or element == "=":
				boolPar = True
			if boolPar == False:
				nomVariable += element
		strbuff = strbuff.replace(nomVariable, "")
		strbuff = strbuff.replace(" ", "")
		strbuff = strbuff.replace("=", "")
		chara = ""
		chara = strbuff[0]
		strbuff = strbuff.replace(chara, "", 1)
		strbuff = strbuff.replace("->", "")
		strbuff = strbuff.replace(")", "")
		
		compiler.write(nomVariable)
		compiler.write(" = Regle(")
		compiler.write(chara)
		compiler.write(", [")
		tableauChara = []
		for element in strbuff:
			if element == "+":
				tableauChara.append("PLUS")
			elif element == "-":
				tableauChara.append("MOINS")
			elif element == "|":
				tableauChara.append("BARRE")
			elif element == "[":
				tableauChara.append("OUVERT")
			elif element == "]":
				tableauChara.append("FERME")
			else:
				tableauChara.append(element)
		for i in range(0, len(tableauChara)-1):
			compiler.write(tableauChara[i])
			compiler.write(", ")
		compiler.write(tableauChara[len(tableauChara)-1])
		compiler.write("])\n")
		
	elif a3 != -1 or boolL == True:
		boolL = True
		L1 = strbuff.find("LSysteme")
		if L1 != -1:
			strbuff = strbuff.replace("LSysteme(", "")
			strbuff = strbuff.replace(")", "")
			nomVariable = str(strbuff)
		L2 = strbuff.find("Alphabet")
		if L2 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Alphabet=", "")
			alphabet = str(strbuff)
		L3 = strbuff.find("Axiome")
		if L3 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Axiome=", "")
			tableauChara = []
			for element in strbuff:
				if element == "+":
					tableauChara.append("PLUS")
				elif element == "-":
					tableauChara.append("MOINS")
				elif element == "|":
					tableauChara.append("BARRE")
				elif element == "[":
					tableauChara.append("OUVERT")
				elif element == "]":
					tableauChara.append("FERME")
				else:
					tableauChara.append(element)
		L4 = strbuff.find("Regles")
		if L4 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Regles=", "")
			regles = str(strbuff)
		L5 = strbuff.find("Pas")
		if L5 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Pas=", "")
			pas = str(strbuff)
		L6 = strbuff.find("Angle")
		if L6 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Angle=", "")
			angle = str(strbuff)
		if strbuff == "}":
			boolL = False
			compiler.write(nomVariable)
			compiler.write(" = LSysteme(")
			compiler.write(alphabet)
			compiler.write(", [")
			for i in range(0, len(tableauChara)-1):
				compiler.write(tableauChara[i])
				compiler.write(", ")
			compiler.write(tableauChara[len(tableauChara)-1])
			compiler.write("], ")
			compiler.write(regles)
			compiler.write(", ")
			compiler.write(pas)
			compiler.write(", ")
			compiler.write(angle)
			compiler.write(")\n")
		
	elif a4 != -1 or boolGenerer == True:
		boolGenerer = True
		L1 = strbuff.find("Generer")
		if L1 != -1:
			strbuff = strbuff.replace("Generer(", "")
			strbuff = strbuff.replace(")", "")
			nomVariable = str(strbuff)
		L2 = strbuff.find("N")
		if L2 != -1:
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("N=", "")
			varN = str(strbuff)
		L3 = strbuff.find("Position")
		if L3 != -1:
			compteurPos += 1
			if compteurPos == 1:
				positionTab = []
				pixelsTab = []
			strbuff = strbuff.replace(" ", "")
			strbuff = strbuff.replace("Position=", "")
			boolPar = False
			position = ""
			for element in strbuff:
				if element == ",":
					boolPar = True
				if boolPar == False:
					position += element
			positionTab.append(position)
			strbuff = strbuff.replace(position, "")
			strbuff = strbuff.replace(",", "")
			pixels = str(strbuff)
			pixelsTab.append(pixels)
		if strbuff == "}":
			boolGenerer = False
			compiler.write(nomVariable)
			compiler.write(".generer(")
			compiler.write(varN)
			compiler.write(")\n")
			for i in range(compteurPos):
				compiler.write(nomVariable)
				compiler.write(".position(")
				compiler.write(positionTab[i])
				compiler.write(", ")
				compiler.write(pixelsTab[i])
				compiler.write(")\n")
			compiler.write(nomVariable)
			compiler.write(".produire()\n")
			
	elif a5 != -1:
		strbuff = strbuff.replace("Fonction(", "")
		strbuff = strbuff.replace(")", "")
		strbuff = strbuff.replace(" ", "")
		nomVariable = ""
		boolPar = False
		for element in strbuff:
			if element == "=":
				boolPar = True
			if boolPar == False:
				nomVariable += element
		strbuff = strbuff.replace(nomVariable, "", 1)
		strbuff = strbuff.replace("=", "")
		chaineNombre = ""
		boolPar = False
		for element in strbuff:
			if element == "n":
				boolPar = True
			if boolPar == False:
				chaineNombre += element
		coefficientDirecteur = int(chaineNombre)
		strbuff = strbuff.replace(chaineNombre, "", 1)
		strbuff = strbuff.replace("n", "")
		ordonneeAlorigine = int(strbuff)
		
		compiler.write(nomVariable)
		compiler.write(" = Fonction(")
		compiler.write(str(coefficientDirecteur))
		compiler.write(", ")
		compiler.write(str(ordonneeAlorigine))
		compiler.write(")\n")
		
	
	contenu = contenu.replace(removeBuff, '', 1)
	strbuff = ""

compiler.write("mainloop()")

compiler.close()
mon_fichier.close()
input()
