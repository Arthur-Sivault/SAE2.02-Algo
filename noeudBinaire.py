from collections import deque


class NoeudBinaire:

    def __init__(self, val=None, g=None, d=None):
        if g!= None: assert isinstance(g, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        if d!= None: assert isinstance(d, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self._valeur = val
        self._gauche = g
        self._droit = d
    
    def get_valeur(self):
        return self._valeur
    
    def get_gauche(self):
        return self._gauche
    
    def get_droit(self):
        return self._droit
    
    def set_valeur(self, val):
        self._valeur = val
    
    def set_gauche(self, g):
        assert isinstance(g, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self._gauche = g
    
    def set_droit(self, d):
        assert isinstance(d, NoeudBinaire), "La racine doit être une instance de la classe NoeudBinaire"
        self._droit = d
    
    def est_vide(self):
        return self._valeur is None and self._gauche is None and self._droit is None 
     
    def possede_gauche(self):
        return self._gauche is not None
    
    def possede_droit(self):
        return self._droit is not None
    
    def est_feuille(self):
        return (not self.est_vide() and self._gauche is None and self._droit is None)
    
    def hauteur(self):
        if self.est_vide():
            return 0
        hauteur_g = self._gauche.hauteur() if self._gauche else 0
        hauteur_d = self._droit.hauteur() if self._droit else 0
        return 1 + max(hauteur_g, hauteur_d)
    
    def __str__(self):
        return
    
    def parcours_prefixe(self):
        if self.est_vide():
            return []
        g = self._gauche.parcours_prefixe() if self._gauche else []
        d = self._droit.parcours_prefixe() if self._droit else []
        return [self._valeur] + g + d
    
    def parcours_infixe(self):
        if self.est_vide():
            return []
        g = self._gauche.parcours_infixe() if self._gauche else []
        d = self._droit.parcours_infixe() if self._droit else []
        return g + [self._valeur] + d
    
    def parcours_suffixe(self):
        if self.est_vide():
            return []
        g = self._gauche.parcours_suffixe() if self._gauche else []
        d = self._droit.parcours_suffixe() if self._droit else []
        return g + d + [self._valeur]
    
    def parcours_largeur(self):
        if self.est_vide():
            return []
    
        res = []
        file = [self]
        
        while file:
            noeud = file.pop(0)
            res.append(noeud.get_valeur())
            
            if noeud.possede_gauche():
                file.append(noeud.get_gauche())
            if noeud.possede_droit():
                file.append(noeud.get_droit())
        return res

