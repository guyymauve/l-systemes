# l-systemes
Projet d'info implémentant un langage pour tracer des L-Systèmes en Python.
## Installation
Clonez le dépôt GitHub et lancez programme.py
## Utilisation
Ecrivez le code dans l'éditeur de texte au milieu. Les boutons sur la gauche de l'écran servent à écrire les squelettes des fonctions principales. Pour lancer le programme, il faut l'interpréter et l'éxecuter, avec l'aide des 3 boutons en haut à droite de la fenêtre (interpréter, lancer, interpréter et lancer). ** Il faut d'abord sauvegarder le programme avant de le compiler, en appuyant sur la disquette**
## Syntaxe
Plusieurs exemples de syntaxe sont fournis dans le dossier exemples pour mieux comprendre la syntaxe.

### Caractere
Permet de créer un nouveau caractère à ajouter à l'alphabet du L-Système et à lui attribuer une instruction pour la tortue.
```
Caractere(<lettre> = <instruction>(<valeur>))
```
* lettre : une lettre majuscule représentant le caractère
* instruction : une instruction parmis les suivantes :
    * NUL : pas d'action
    * FORWARD : avance
    * BACKWARD : recul
    * LEFT : tourne à gauche
    * RIGHT : tourne à droite
    * ROLL : tourne de 180°
    * SAVE : sauvegarde la postion actuelle et la place en haut de la pile de suavegardes
    * LOAD : revient à la dernière position sauvegardée et la dépile
* valeur : pour FORWARD, BACKWARD, LEFT et RIGHT, cela permet de rentre la valeur du pas de la tortue, soit en pixels pour les translations, soit en angle pour les rotations. Si elle vaut 0, le pas/angle de base du L-Système sera utilisé.

ex: On définit A qui s'interpréte comme "tourner à droite de 30°
```
Caractère(A = RIGHT(30))
```

### Règle
Permet de créer une règle d'évolution du caractère.
```
Regle(<nom> = <caractere>-><caracteres>)
```
* nom : nom de la règle (string)
* caractere: un caractère déjà défini
* caracteres : une suite de caractères et de constantes. Les constantes ont comme les caractères des propriétés interprétées par la tortue mais ne peuvent pas évoluer selon des règles. Les constantes possibles sont :
    * \+ (équivalent de LEFT)
    * \- (équivalent de RIGHT)
    * | (équivalent de ROLL)
    * [ (équivalent de SAVE)
    * ] (équivalent de LOAD)

ex: On définit la règle R1 qui dit que A se transforme en A+B-A
```
Regle(R1 = A->A+B-A)
```

### L-Système
Une fois les caractères et règles définies, on peut construire le L-Sytème que l'on veut.

```
LSysteme(<nom>)
{
	Alphabet = <alphabet>
	Axiome = <axiome>
	Regles = <regles>
	Pas = <pas>
	Angle = <angle>
}
```
* nom : nom du L-Sytème
* alphabet : tableau de caractères
* axiome : chaîne de caractères/constantes qui est le L-Sytème à l'itération 0
* regles : tableau de regles
* pas : pas par défaut de la tortue en pixels
* angles : angle par défaut de la tortue en degrés

ex : Triangle de Sierpinski
```
Caractere(F = FORWARD(0))
Caractere(G = FORWARD(0))

Regle(R1 = F->F-G+F+G-F)
Regle(R2 = G->GG)

LSysteme(Sierpinski)
{
	Alphabet = [F, G]
	Axiome = F-G-G
	Regles = [R1, R2]
	Pas = 5
	Angle = 120
}
```

## Génerer
Une fois le L-Système créé, on peut le générer et le tracer.

```
Generer(<nom>)
{
    N = <n>
    [Position = <pos>]
}
```
* nom : nom du L-Système à générer
* n : nombre d'itérations
Arguments facultatifs :
* pos : indique où la tortue doit démarrer son chemin. Par exemple, "HAUT, 20" la fait démarrer à 20 pixels du haut de l'écran

ex:
```
Generer(Sierpinski)
{
	N = 8
}
```