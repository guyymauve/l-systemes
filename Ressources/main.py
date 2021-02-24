from Caractere import *

# A = Caractere("A", FORWARD, 10, 0)
# B = Caractere("B", RIGHT, 10, 0)
# R1 = Regle(A, [A,B])
# R2 = Regle(B, [A])

# Algue = LSysteme([A, B], [A], [R1, R2], 100, 30)
# Algue.generer(20)
# Algue.produire()

# R3 = Regle(A, [A, PLUS, A, MOINS, A, MOINS, A, PLUS, A])

# Koch = LSysteme([A], [A], [R3], 5, 85)
# Koch.afficher()

# F = Caractere("F", FORWARD)
# X = Caractere("X", NUL)
# Y = Caractere("Y", NUL)
# R4 = Regle(X, [X, PLUS, Y, F, PLUS])
# R5 = Regle(Y, [MOINS, F, X, MOINS, Y])

# Dragon = LSysteme([X, Y, F], [F, X], [R4, R5], 5, 90)
# Dragon.afficher()

# G = Caractere("G", FORWARD)
# R6 = Regle(F, [F, MOINS, G, PLUS, F, PLUS, G, MOINS, F])
# R7 = Regle(G, [G, G])

# Sierpinski = LSysteme([F, G], [F, MOINS, G, MOINS, G], [R6, R7], 5, 120)
# Sierpinski.afficher()

# UN = Caractere("1", FORWARD, 0, 0)
# ZERO = Caractere("0", FORWARD, 0, 0)
# R8 = Regle(UN, [UN, UN])
# R9 = Regle(ZERO, [UN, OUVERT, PLUS, ZERO, FERME, MOINS, ZERO])

# Pythagore = LSysteme([ZERO, UN], [ZERO], [R8, R9], 10, 30)
# Pythagore.afficher()
# Pythagore.generer(7)
# Pythagore.position(GAUCHE, 0)
# Pythagore.produire()

# U = Caractere("U", FORWARD)
# V = Caractere("V", FORWARD)

# RA = Regle(U, [U, PLUS, V, MOINS, U])
# RB = Regle(V, [V, PLUS, OUVERT, U, FERME, MOINS, V])

# Random = LSysteme([U, V], [U], [RA, RB], 5, 30)
# Random.afficher()

# f1 = Fonction(3, 2)

# M = Caractere("M", FORWARD, 0, 0)
# N = Caractere("N", FORWARD, 0, 0)
# L = Caractere("L", FORWARD, 0, 0)

# RM = Regle(M, [L, PLUS, N])
# RN = Regle(N, [M, MOINS, L])
# RL = Regle(L, [N, PLUS, M])

# Yolo = LSysteme([L, M, N], [L], [RL, RM, RN], 10, 10)

# Yolo.generer(20)
# Yolo.position(DROITE, 200)
# Yolo.position(BAS, 100)
# Yolo.produire()





input()