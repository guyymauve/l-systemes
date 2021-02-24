from Caractere import *

X = Caractere("X", NUL, 0, 0)
Y = Caractere("Y", NUL, 0, 0)
F = Caractere("F", FORWARD, 0, 0)
R1 = Regle(X, [X, PLUS, Y, F, PLUS])
R2 = Regle(Y, [MOINS, F, X, MOINS, Y])
Dragon = LSysteme([X,Y,F], [F, X], [R1,R2], 5, 90)
Dragon.generer(11)
Dragon.produire()
mainloop()