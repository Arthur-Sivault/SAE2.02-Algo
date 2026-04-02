from noeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    def __init__(self, caracteres, poids, g=None, d=None):
        super().__init__((caracteres, poids), g, d) # on appelle NoeudBinaire.__init__ 
        self.valeur = (caracteres, poids) # dans la classe NoeudHuffman, la valeur constitue le tuple (caracteres, poids)

    # Getters
    def get_caracteres(self):
        return self.valeurs[0] # premier element du tuple (caracteres, poids)
    
    def get_poids(self):
        return self.valeurs[1] # deuxième element du tuple (caracteres, poids)

    # Setters
    def set_caracteres(self, caracteres):
        self.valeur = (caracteres, self.valeur[1])

    def set_poids(self, poids): 
        self.valeur = (self.valeur[0], poids)

    # Méthode permettant de construire l'arbre de Huffman à partir d'une chaine de caractères 
    def construire_arbre_huffman(self, caracteres):
        # On commence par créer le dictionnaire dont les éléments sont les couples (caractere, effectif du caractere)
        effectif_dictionnaire = {}                    
        for c in caracteres:
            if c in effectif_dictionnaire:
                effectif_dictionnaire[c] += 1
            else:
                effectif_dictionnaire[c] = 1


        # On veut une liste donc on met les éléments du dictionnaire dans une liste L
        L = []
        for c in effectif_dictionnaire:
            L.append((c, effectif_dictionnaire[c]))
        L = sorted(L, key=lambda x: x[1], reverse=True) # on trie la liste L par ordre décroissant d'effectif
        return L


    
        