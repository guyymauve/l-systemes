from Caractere import *

A = Caractere("A", FORWARD, 0, 0)
B = Caractere("B", FORWARD, 0, 0)
R1 = Regle(A, [A, PLUS, B, PLUS, PLUS, OUVERT, MOINS, MOINS, A, B, FERME, MOINS, A])
R2 = Regle(B, [B, B])
Gootie = LSysteme([A,B], [A], [R1,R2], 10, 30)
Gootie.generer(5)
Gootie.produire()
mainloop()