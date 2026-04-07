from NoeudBinaire import NoeudBinaire
from NoeudHuffman import NoeudHuffman

g = NoeudBinaire('G', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
# Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
f = NoeudBinaire('F', g, None)
# Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
e = NoeudBinaire('E', None, f)
# Arbre de valeur 'D', sans sous-arbres (feuille)
d = NoeudBinaire('D', None, None)
# Arbre de valeur 'C', sans sous-arbres (feuille)
c = NoeudBinaire('C', None, None)
# Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
b = NoeudBinaire('B', c, d)
# Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
a = NoeudBinaire('A', b, e)
mon_arbre = a
print("Affichage NoeudBinaire : ")
print(mon_arbre)

s = "bonjourbonsoir"
print("Affichage NoeudHuffman : ")
arbre = NoeudHuffman.construire_arbre(s)
print(arbre)

codes = arbre.generer_codes()
print(codes)