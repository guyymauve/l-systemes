from Caractere import *

F = Caractere("F", FORWARD, 0, 0)
G = Caractere("G", FORWARD, 0, 0)
R1 = Regle(F, [F, MOINS, G, PLUS, F, PLUS, G, MOINS, F])
R2 = Regle(G, [G, G])
Sierpinski = LSysteme([F,G], [F, MOINS, G, MOINS, G], [R1,R2], 5, 120)
Sierpinski.generer(8)
Sierpinski.produire()
mainloop()