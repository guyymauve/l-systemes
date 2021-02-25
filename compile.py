from Caractere import *

A = Caractere("A", FORWARD, 0, 0)
B = Caractere("B", FORWARD, 0, 0)
R1 = Regle(A, [A, MOINS, B, MOINS, MOINS, B, PLUS, A, PLUS, PLUS, A, A, PLUS, B, MOINS])
R2 = Regle(B, [PLUS, A, MOINS, B, B, MOINS, MOINS, B, MOINS, A, PLUS, PLUS, A, PLUS, B])
Gosper = LSysteme([A,B], [A], [R1,R2], 5, 60)
Gosper.generer(4)
Gosper.position(HAUT, 100)
Gosper.produire()
mainloop()