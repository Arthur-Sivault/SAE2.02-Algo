class NoeudBinaire:
    def __init__(self, val, g=None, d=None):
        assert type(val) == str, "La valeur doit être une chaîne de caractères"
        if g!= None: assert isinstance(g, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        elif d!= None: assert isinstance(d, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self.valeur = val
        self.gauche = g
        self.droit = d
    
    def get_valeur(self):
        return self.valeur
    
    def get_gauche(self):
        return self.gauche
    
    def get_droit(self):
        return self.droit
    
    def set_valeur(self, val):
        assert type(val) == str, "La valeur doit être une chaîne de caractères"
        self.valeur = val
    
    def set_gauche(self, g):
        assert isinstance(g, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self.gauche = g
    
    def set_droit(self, d):
        assert isinstance(d, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self.droit = d
    
    def est_vide(self):
        return self.valeur is None
     
    def possede_gauche(self):
        return self.gauche is not None
    
    def possede_droit(self):
        return self.droit is not None
    
    def est_feuille(self):
        return (not self.est_vide() and self.gauche is None and self.droit is None)
    
    def hauteur(self):
        if self.est_vide():
            return 0
        hauteur_g = self.gauche.hauteur() if self.gauche else 0
        hauteur_d = self.droit.hauteur() if self.droit else 0
        return 1 + max(hauteur_g, hauteur_d)
    
    def __str__(self):
        return