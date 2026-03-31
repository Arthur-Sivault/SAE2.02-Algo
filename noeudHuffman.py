from noeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    def __init__(self, caracteres, poids, g=None, d=None):
        super().__init__((caracteres, poids), g, d) # on appelle NoeudBinaire.__init__ 
        self.valeur = (caracteres, poids) # dans la classe NoeudHuffman, la valeur constitue le tuple (caracteres, poids)

    # Getters
    def get_caracteres(self):
        return self.caracteres
    
    def get_poids(self):
        return self.poids
    
    # Setters
    def set_caracteres(self, caracteres):
        self.caracteres = caracteres

    def set_poids(self, poids): 
        self.poids = poids

    # Méthode permettant de construire l'arbre de Huffman à partir d'une chaine de caractères 
    def construire_arbre_huffman(self):
        
        pass