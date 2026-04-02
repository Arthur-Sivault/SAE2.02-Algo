class NoeudBinaire:

    def __init__(self, val=None, g=None, d=None):
        """Initialise un noeud binaire avec une valeur et des sous-arbres gauche et droit. Si rien n'est précisé, la valeur par défault en None"""
        if g!= None: assert isinstance(g, NoeudBinaire), "Le sous-arbre gauche doit être une instance de la classe NoeudBinaire"
        if d!= None: assert isinstance(d, NoeudBinaire), "Le sous-arbre droit doit être une instance de la classe NoeudBinaire"
        self._valeur = val
        self._gauche = g
        self._droit = d
    
    def get_valeur(self):
        """Retourne la valeur du noeud."""
        return self._valeur
    
    def get_gauche(self):
        """Retourne le sous-arbre gauche."""
        return self._gauche
    
    def get_droit(self):
        """Retourne le sous-arbre droit."""
        return self._droit
    
    def set_valeur(self, val):
        """Modifie la valeur du noeud."""
        self._valeur = val
    
    def set_gauche(self, g):
        """Modifie le sous-arbre gauche."""
        assert isinstance(g, NoeudBinaire), "Le sous-arbre gauche doit être une instance de la classe NoeudBinaire"
        self._gauche = g
    
    def set_droit(self, d):
        """Modifie le sous-arbre droit."""
        assert isinstance(d, NoeudBinaire), "Le sous-arbre droit doit être une instance de la classe NoeudBinaire"
        self._droit = d
    
    def est_vide(self):
        """Retourne True si le noeud est vide (sans valeur et sans sous-arbre), False sinon."""
        return self._valeur is None and self._gauche is None and self._droit is None 
     
    def possede_gauche(self):
        """Retourne True si le noeud possède un sous-arbre gauche, False sinon."""
        return self._gauche is not None
    
    def possede_droit(self):
        """Retourne True si le noeud possède un sous-arbre droit, False sinon."""
        return self._droit is not None
    
    def est_feuille(self):
        """Retourne True si le noeud est une feuille (sans sous-arbre), False sinon."""
        return (not self.est_vide() and self._gauche is None and self._droit is None)
    
    def hauteur(self):
        """Retourne la hauteur de l'arbre binaire."""
        if self.est_vide():
            return 0
        hauteur_g = self._gauche.hauteur() if self._gauche else 0
        hauteur_d = self._droit.hauteur() if self._droit else 0
        return 1 + max(hauteur_g, hauteur_d)
    
    def __str__(self):
        """Retourne la représentation textuelle de l'arbre binaire en utilisant _generer_affichage"""
        return self._generer_affichage(0)

    def _generer_affichage(self, niveau):
        """Méthode qui génère la représentation textuelle de l'arbre.Chaque noeud est affiché avec une indentation 
        proportionnelle à son niveau dans l'arbre. Le paramètre niveau indique la profondeur du noeud courant 0 est pour la racine"""
        if self.est_vide(): return ""
        if niveau == 0 :
            res = str(self._valeur) + "\n"
        else:
            res = "    " * (niveau-1) + "|-->" + str(self._valeur) + "\n"
        if self.possede_gauche():
                res += self._gauche._generer_affichage(niveau +1)
        if self.possede_droit():
                res += self._droit._generer_affichage(niveau +1)
        return res


    def parcours_prefixe(self):
        """Retourne la liste des valeurs du parcours préfixe de l'arbre."""
        if self.est_vide():
            return []
        g = self._gauche.parcours_prefixe() if self._gauche else []
        d = self._droit.parcours_prefixe() if self._droit else []
        return [self._valeur] + g + d
    
    def parcours_infixe(self):
        """Retourne la liste des valeurs du parcours infixe de l'arbre."""
        if self.est_vide():
            return []
        g = self._gauche.parcours_infixe() if self._gauche else []
        d = self._droit.parcours_infixe() if self._droit else []
        return g + [self._valeur] + d
    
    def parcours_suffixe(self):
        """Retourne la liste des valeurs du parcours suffixe de l'arbre."""
        if self.est_vide():
            return []
        g = self._gauche.parcours_suffixe() if self._gauche else []
        d = self._droit.parcours_suffixe() if self._droit else []
        return g + d + [self._valeur]
    
    def parcours_largeur(self):
        """Retourne la liste des valeurs du parcours en largeur de l'arbre."""
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
